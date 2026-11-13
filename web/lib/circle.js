// Circle community step: look the email up, invite it if it is new, and tag it.
// Uses Circle's Admin API v2. Needs CIRCLE_API_TOKEN (Circle: Settings > Developers > Tokens).
// Without a token it runs in dry-run mode and reports what it would have done.
//
// NOT YET VERIFIED AGAINST A LIVE COMMUNITY. Circle's public docs confirm the endpoints
// (POST /community_members, GET /community_members/search) and the Bearer header, but not
// every field name, so run `npm run check:circle` with a real token before launch.
'use strict';

const BASE = process.env.CIRCLE_API_BASE || 'https://app.circle.so/api/admin/v2';
const ids = (v) => (v || '').split(',').map((x) => Number(x.trim())).filter(Boolean);

async function call(method, path, body) {
  const scheme = process.env.CIRCLE_AUTH_SCHEME || 'Bearer';
  const res = await fetch(BASE + path, {
    method,
    headers: { Authorization: `${scheme} ${process.env.CIRCLE_API_TOKEN}`, 'Content-Type': 'application/json' },
    body: body ? JSON.stringify(body) : undefined,
    signal: AbortSignal.timeout(10000),
  });
  let data = null;
  try { data = await res.json(); } catch { /* empty body */ }
  return { status: res.status, ok: res.ok, data };
}

async function findMember(email) {
  const r = await call('GET', `/community_members/search?email=${encodeURIComponent(email)}`);
  if (r.status === 404) return null;
  if (!r.ok) throw new Error(`circle search failed: ${r.status}`);
  const m = r.data && (r.data.records ? r.data.records[0] : r.data);
  return m && m.id ? m : null;
}

// Returns { mode: 'dry_run' | 'live', status: 'invited' | 'already_member' | 'failed', detail }
async function addToCommunity({ email, name }) {
  if (!process.env.CIRCLE_API_TOKEN) return { mode: 'dry_run', status: 'invited', detail: 'CIRCLE_API_TOKEN not set' };
  try {
    const existing = await findMember(email);
    if (existing) return { mode: 'live', status: 'already_member', detail: String(existing.id) };
    const r = await call('POST', '/community_members', {
      email,
      name: name || undefined,
      skip_invitation: false,
      space_ids: ids(process.env.CIRCLE_SPACE_IDS),
      member_tag_ids: ids(process.env.CIRCLE_TAG_IDS),
    });
    if (!r.ok) return { mode: 'live', status: 'failed', detail: `HTTP ${r.status}: ${JSON.stringify(r.data).slice(0, 200)}` };
    return { mode: 'live', status: 'invited', detail: String((r.data && (r.data.community_member || r.data).id) || '') };
  } catch (e) {
    return { mode: 'live', status: 'failed', detail: e.message };
  }
}

module.exports = { addToCommunity, findMember, configured: () => Boolean(process.env.CIRCLE_API_TOKEN) };
