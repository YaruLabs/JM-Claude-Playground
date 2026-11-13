// Sends the "your 20 ideas" email through Resend (RESEND_API_KEY + EMAIL_FROM).
// Without a key it writes the email to web/.outbox/ so the flow can be tested end to end.
'use strict';
const fs = require('fs');
const path = require('path');

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function render({ name, ideas, link, communityUrl }) {
  const rows = ideas.map((i, n) => `
    <tr><td style="padding:14px 0;border-top:1px solid #e4ddcd">
      <div style="font:700 16px/1.3 Arial,sans-serif;color:#1f150b">${n + 1}. ${esc(i.name)}</div>
      <div style="font:14px/1.5 Arial,sans-serif;color:#5a4632;margin-top:4px">${esc(i.one_liner)}</div>
      <div style="font:13px/1.5 Arial,sans-serif;color:#5a4632;margin-top:6px"><b>Why it works:</b> ${esc(i.why_it_works)}</div>
    </td></tr>`).join('');
  const html = `<!doctype html><html><body style="margin:0;background:#f9f3ea">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td align="center" style="padding:24px 12px">
  <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;background:#fffdf9;border:1px solid #e4ddcd;border-radius:10px">
    <tr><td style="padding:28px 28px 8px">
      <div style="font:700 13px Arial,sans-serif;letter-spacing:.08em;color:#d12d40">YARU LABS</div>
      <h1 style="font:700 24px/1.25 Arial,sans-serif;color:#1f150b;margin:10px 0 8px">Your 20 startup ideas${name ? ', ' + esc(name) : ''}</h1>
      <p style="font:15px/1.6 Arial,sans-serif;color:#5a4632;margin:0 0 16px">Matched to your quiz answers. Each one opens with its sources, what AI agents handle, the part that stays with you, and your first three steps.</p>
      <a href="${esc(link)}" style="display:inline-block;background:#d12d40;color:#fffdf9;font:700 15px Arial,sans-serif;text-decoration:none;padding:13px 22px;border-radius:8px">Open your ideas and the full database</a>
      <p style="font:13px/1.5 Arial,sans-serif;color:#5a4632;margin:14px 0 0">This link is yours. Keep this email to come back to it.</p>
    </td></tr>
    <tr><td style="padding:8px 28px 8px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">${rows}</table></td></tr>
    <tr><td style="padding:16px 28px 28px;border-top:1px solid #e4ddcd">
      <p style="font:14px/1.6 Arial,sans-serif;color:#5a4632;margin:0">You also have an invite to the Yaru community${communityUrl ? ` (<a href="${esc(communityUrl)}" style="color:#d12d40">open it here</a>)` : ''}. Check your inbox for a separate email from Circle to set your password.</p>
      <p style="font:12px/1.5 Arial,sans-serif;color:#78593a;margin:14px 0 0">These ideas are researched starting points, not guarantees. Check the "watch out" note on each before you build.</p>
    </td></tr>
  </table></td></tr></table></body></html>`;
  const text = `Your 20 startup ideas\n\nOpen them, with the full database: ${link}\n\n` +
    ideas.map((i, n) => `${n + 1}. ${i.name}: ${i.one_liner}`).join('\n');
  return { html, text };
}

// Returns { mode: 'dry_run' | 'live', ok, detail }
async function sendIdeas({ to, name, ideas, link }) {
  const { html, text } = render({ name, ideas, link, communityUrl: process.env.CIRCLE_COMMUNITY_URL });
  const subject = 'Your 20 startup ideas are ready';
  if (!process.env.RESEND_API_KEY) {
    const dir = path.join(__dirname, '..', '.outbox');
    try {
      fs.mkdirSync(dir, { recursive: true });
      fs.writeFileSync(path.join(dir, `${Date.now()}-${to.replace(/[^a-z0-9]/gi, '_')}.html`), `<!-- to: ${to} | subject: ${subject} -->\n${html}`);
    } catch { /* read-only filesystem (serverless): nothing to write to */ }
    return { mode: 'dry_run', ok: true, detail: 'RESEND_API_KEY not set' };
  }
  try {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from: process.env.EMAIL_FROM || 'Yaru Labs <ideas@yaru.ai>', to: [to], subject, html, text }),
      signal: AbortSignal.timeout(10000),
    });
    return { mode: 'live', ok: res.ok, detail: res.ok ? '' : `HTTP ${res.status}: ${(await res.text()).slice(0, 200)}` };
  } catch (e) {
    return { mode: 'live', ok: false, detail: e.message };
  }
}

module.exports = { sendIdeas, render, configured: () => Boolean(process.env.RESEND_API_KEY) };
