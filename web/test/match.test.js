// Matcher checks: every answer combination must return 2 + 20 ideas that respect the hard limits.
'use strict';
const assert = require('assert');
const ideas = require('../data/ideas.json');
const { QUIZ, rank, validate } = require('../lib/match');
const { sign, verify } = require('../lib/token');

let seed = 42;
const rnd = () => (seed = (seed * 1664525 + 1013904223) % 4294967296) / 4294967296;
const pick = (arr) => arr[Math.floor(rnd() * arr.length)];
function randomAnswers() {
  const a = {};
  for (const q of QUIZ.questions) {
    const ids = q.options.map((o) => o.id);
    a[q.id] = q.type === 'multi' ? [...new Set([pick(ids), pick(ids), pick(ids)])].slice(0, 1 + Math.floor(rnd() * q.max)) : pick(ids);
  }
  return a;
}
const TECH = { none: 0, some: 1, builder: 2 };
const relaxCount = [0, 0, 0], byWhere = {};
const N = 3000;
for (let n = 0; n < N; n++) {
  const a = randomAnswers();
  const r = rank(ideas, a);
  assert.strictEqual(r.top.length, 2, `2 ideas for ${JSON.stringify(a)}`);
  assert.strictEqual(r.more.length, 20, `20 more for ${JSON.stringify(a)} (pool ${r.pool})`);
  const all = [...r.top, ...r.more];
  assert.strictEqual(new Set(all.map((p) => p.idea.id)).size, 22, 'no repeats');
  for (const p of all) {
    const t = p.idea.tags;
    assert(!(a.tech === 'none' && t.tech === 'builder'), 'non-technical people never get engineering-heavy ideas');
    assert(TECH[t.tech] - TECH[a.tech] <= 1);
    assert(t.budget - Number(a.budget) <= 2 && t.hours - Number(a.hours) <= 2);
    if (a.where === 'th_expat') assert(t.thai_language !== 'required', 'expat-facing founders never need Thai');
  }
  assert.notStrictEqual(r.top[0].idea.tags.interests[0], r.top[1].idea.tags.interests[0], 'top 2 differ in subject');
  relaxCount[r.relax]++;
  (byWhere[a.where] = byWhere[a.where] || { n: 0, native: 0 }).n++;
  byWhere[a.where].native += r.top.filter((p) => p.fit === 'native').length / 2;
  // same answers -> same result (stateless recompute must be stable)
  if (n < 50) assert.deepStrictEqual(rank(ideas, a).more.map((p) => p.idea.id), r.more.map((p) => p.idea.id));
}
assert.throws(() => validate({ where: 'mars' }), /bad answer/);
assert.throws(() => rank(ideas, { ...randomAnswers(), interests: ['money', 'health', 'pets', 'food'] }), /bad answer/);
const tok = sign({ a: 1, t: Date.now() });
assert.deepStrictEqual(verify(tok).a, 1);
assert.strictEqual(verify(tok.slice(0, -2) + 'xx'), null, 'tampered code rejected');
assert.strictEqual(verify('junk'), null);
console.log(`ok: ${N} random quiz runs over ${ideas.length} ideas`);
console.log('pool widening needed (0 none, 1 adapt other markets, 2 loosen limits):', relaxCount.map((c) => `${(100 * c / N).toFixed(0)}%`).join(' / '));
for (const [w, v] of Object.entries(byWhere)) console.log(`  ${w.padEnd(9)} top-2 from the visitor's own market: ${(100 * v.native / v.n).toFixed(0)}%`);
