// POST /api/match { answers } -> two full ideas, teaser names for 20 more, and a signed
// code that carries the answers (so nothing is stored until the visitor joins).
'use strict';
const ideas = require('../lib/library');
const { rank, present } = require('../lib/match');
const { sign, verify } = require('../lib/token');
const { limited, body } = require('../lib/http');

module.exports = async (req, res) => {
  if (req.method !== 'POST') return res.status(405).json({ error: 'POST only' });
  if (limited(req, 'match', 30, 60e3)) return res.status(429).json({ error: 'Too many requests. Try again in a minute.' });
  const b = body(req);
  // A returning visitor sends their code instead of answers.
  const fromToken = b.token ? verify(b.token) : null;
  let r;
  try { r = rank(ideas, fromToken ? fromToken.a : b.answers); }
  catch (e) { return res.status(400).json({ error: e.message }); }
  if (r.relax > 0) console.log(JSON.stringify({ event: 'coverage_gap', relax: r.relax, pool: r.pool, answers: r.answers }));
  res.status(200).json({
    token: sign({ a: r.answers, t: Date.now() }),
    ideas: r.top.map(present),
    more: r.more.map((p) => ({ name: p.idea.name, area: p.idea.tags.interests[0] })),
    library_size: ideas.length,
  });
};
