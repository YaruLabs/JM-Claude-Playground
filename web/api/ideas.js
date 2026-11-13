// GET /api/ideas?m=<member code> -> the member's matched ideas and the full database.
'use strict';
const ideas = require('../lib/library');
const { rank, present } = require('../lib/match');
const { verify } = require('../lib/token');
const { limited } = require('../lib/http');

module.exports = async (req, res) => {
  if (limited(req, 'ideas', 30, 60e3)) return res.status(429).json({ error: 'Too many requests.' });
  const m = new URL(req.url, 'http://x').searchParams.get('m');
  const p = verify(m);
  if (!p || !p.m) return res.status(401).json({ error: 'This link is not valid. Take the quiz and join to get your own.' });
  const r = rank(ideas, p.a);
  const mine = [...r.top, ...r.more];
  const mineIds = new Set(mine.map((x) => x.idea.id));
  res.setHeader('Cache-Control', 'private, no-store');
  res.status(200).json({
    mine: mine.map(present),
    all: ideas.filter((i) => !mineIds.has(i.id)).map((idea) => present({ idea, fit: 'native', reasons: [] })),
  });
};
