// POST /api/join { email, name?, token, consent } -> invites the email to the Circle
// community and emails the visitor their 20 ideas plus a personal link to the database.
'use strict';
const crypto = require('crypto');
const ideas = require('../lib/library');
const { rank } = require('../lib/match');
const { sign, verify } = require('../lib/token');
const circle = require('../lib/circle');
const mail = require('../lib/email');
const { limited, origin, body } = require('../lib/http');

const EMAIL = /^[^\s@]{1,64}@[^\s@]{1,190}\.[a-z]{2,}$/i;

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'POST only' });
  if (limited(req, 'join', 6, 10 * 60e3)) return res.status(429).json({ error: 'Too many attempts. Try again in a few minutes.' });
  const b = body(req);
  if (b.website) return res.status(200).json({ ok: true }); // honeypot field: bots fill it, people never see it
  const email = String(b.email || '').trim().toLowerCase();
  const name = String(b.name || '').trim().slice(0, 80);
  if (!EMAIL.test(email)) return res.status(400).json({ error: 'That email address does not look right.' });
  if (b.consent !== true) return res.status(400).json({ error: 'Please tick the box to join.' });
  const quiz = verify(b.token);
  if (!quiz) return res.status(400).json({ error: 'Your quiz result expired. Please retake the quiz.' });

  const r = rank(ideas, quiz.a);
  const member = sign({ a: r.answers, e: crypto.createHash('sha256').update(email).digest('hex').slice(0, 16), t: Date.now(), m: 1 });
  const link = `${origin(req)}/ideas.html?m=${member}`;

  const [community, sent] = await Promise.all([
    circle.addToCommunity({ email, name }),
    mail.sendIdeas({ to: email, name, link, ideas: r.more.map((p) => p.idea) }),
  ]);
  const lead = { event: 'lead', ts: new Date().toISOString(), email, name, answers: r.answers, circle: community.status, circle_mode: community.mode, email_sent: sent.ok, email_mode: sent.mode };
  console.log(JSON.stringify({ ...lead, email: email.replace(/^(.).*(@.*)$/, '$1***$2') }));
  if (community.status === 'failed') console.error('circle:', community.detail);
  if (!sent.ok) console.error('email:', sent.detail);
  if (process.env.LEADS_WEBHOOK_URL) {
    fetch(process.env.LEADS_WEBHOOK_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(lead), signal: AbortSignal.timeout(5000) }).catch(() => {});
  }
  if (!sent.ok) return res.status(502).json({ error: 'We could not send your email just now. Please try again in a minute.' });
  const out = { ok: true, community: community.status };
  // With no email provider configured there is no inbox to check, so hand the link back for testing.
  if (sent.mode === 'dry_run') out.dev_link = link;
  res.status(200).json(out);
};
