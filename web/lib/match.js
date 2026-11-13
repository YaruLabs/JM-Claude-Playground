// Deterministic quiz-to-idea matcher. No AI call: the research cost was paid when the
// library was built, so matching a visitor costs nothing.
// Used by the site (api/*.js) and by the /startup-ideas skill (node web/lib/match.js).
'use strict';
const crypto = require('crypto');
const QUIZ = require('./quiz.json');

const MARKETS = {
  th_local: ['TH_LOCAL'], th_expat: ['TH_EXPAT'], th_both: ['TH_LOCAL', 'TH_EXPAT'],
  us: ['US'], uk: ['UK'], anywhere: ['GLOBAL', 'US', 'UK'],
};
const TECH = { none: 0, some: 1, builder: 2 };
const LABEL = {};
for (const q of QUIZ.questions) for (const o of q.options) LABEL[`${q.id}:${o.id}`] = o.label;

// Returns a cleaned answers object, or throws with a message naming the bad field.
function validate(raw) {
  const a = {};
  for (const q of QUIZ.questions) {
    const ids = new Set(q.options.map((o) => o.id));
    const v = raw ? raw[q.id] : undefined;
    if (q.type === 'multi') {
      const list = Array.isArray(v) ? [...new Set(v.map(String))] : [];
      if (!list.length || list.length > q.max || !list.every((x) => ids.has(x))) throw new Error(`bad answer: ${q.id}`);
      a[q.id] = list.sort();
    } else {
      if (!ids.has(String(v))) throw new Error(`bad answer: ${q.id}`);
      a[q.id] = String(v);
    }
  }
  return a;
}

function eligibility(idea, a, relax) {
  const t = idea.tags;
  const want = MARKETS[a.where];
  const native = t.markets.some((m) => want.includes(m));
  const global = t.markets.includes('GLOBAL');
  let fit = native ? 'native' : global ? 'global' : t.portable ? 'adapt' : null;
  if (!fit) return null;
  if (fit === 'adapt' && relax < 1) return null;               // adaptations only when the pool is thin
  if (a.where === 'th_expat' && t.thai_language === 'required') return null;
  const slack = relax >= 2 ? 1 : 0;
  if (TECH[t.tech] - TECH[a.tech] > (a.tech === 'none' ? 1 : 1)) return null;
  if (t.tech === 'builder' && a.tech === 'none') return null;
  if (t.budget - Number(a.budget) > 1 + slack) return null;
  if (t.hours - Number(a.hours) > 1 + slack) return null;
  if (a.automation === 'agents' && (t.agent_share < 70 - 10 * slack)) return null;
  if (a.automation === 'balanced' && t.agent_share < 55 - 10 * slack) return null;
  return fit;
}

function score(idea, a, fit) {
  const t = idea.tags;
  let s = fit === 'native' ? 30 : fit === 'global' ? 20 : 6;
  const reasons = [];
  const shared = t.interests.filter((i) => a.interests.includes(i));
  s += Math.min(shared.length, 2) * 14;
  if (shared.length) reasons.push(['interest', `You picked ${LABEL['interests:' + shared[0]].toLowerCase()}, and this sits right in it.`]);
  if (a.customer === 'any') s += 5;
  else if (t.customer === a.customer) { s += 12; }
  else s -= 6;
  if (a.channel === 'any') s += t.channels.includes('content') ? 6 : 3;
  else if (t.channels.includes(a.channel)) {
    s += 14;
    reasons.push(['channel', {
      content: 'It grows through content, which is how you said you want to find customers.',
      seo: 'People already search for this, so useful pages can bring customers to you.',
      community: 'Its customers gather in groups you can join and help in.',
      outbound: 'You can reach its buyers directly, which suits how you like to sell.',
    }[a.channel]]);
  }
  if (t.backgrounds.includes(a.background) && a.background !== 'any') {
    s += 13;
    reasons.push(['background', `Your ${LABEL['background:' + a.background].toLowerCase()} background is an edge here.`]);
  } else if (t.backgrounds.includes('any')) s += 5;
  if (t.goals.includes(a.goal)) s += 10;
  const techGap = TECH[t.tech] - TECH[a.tech];
  s += techGap > 0 ? -8 : 4;
  if (t.tech === 'none' && a.tech === 'none') reasons.push(['tech', 'You can ship a first version with no-code AI tools.']);
  const budgetGap = t.budget - Number(a.budget);
  const hoursGap = t.hours - Number(a.hours);
  s += budgetGap > 0 ? -8 * budgetGap : 3;
  s += hoursGap > 0 ? -8 * hoursGap : 3;
  if (hoursGap <= 0 && Number(a.hours) <= 2) reasons.push(['hours', 'It fits the hours you have each week.']);
  const autoWeight = { agents: 16, balanced: 9, hands_on: 3 }[a.automation];
  s += ((t.agent_share - 60) / 35) * autoWeight;
  if (t.agent_share >= 80 && a.automation !== 'hands_on') reasons.push(['agents', `Agents can run about ${t.agent_share}% of the ongoing work (est.).`]);
  if (a.automation === 'hands_on' && t.local_presence) s += 4;
  if (a.goal === 'side_income' && t.speed === 'weeks') { s += 5; reasons.push(['speed', 'A first paying customer is realistic within weeks, not months.']); }
  const q = idea.quality;
  s += (q.status === 'RECOMMENDED' ? 10 : 0) + (q.set === 'new' ? 6 : 0) + (q.score - 3) * 8;
  if (fit === 'adapt') reasons.unshift(['adapt', 'It was researched for another market, so you would adapt it to yours.']);
  return { s, reasons };
}

// Stable per-visitor tie-break so equal scores don't always show the same idea.
function jitter(id, a) {
  const h = crypto.createHash('sha256').update(id + JSON.stringify(a)).digest();
  return h[0] / 255;
}

function rank(ideas, answers) {
  const a = validate(answers);
  let pool = [], relax = 0;
  for (; relax <= 2; relax++) {
    pool = [];
    for (const idea of ideas) {
      const fit = eligibility(idea, a, relax);
      if (!fit) continue;
      const { s, reasons } = score(idea, a, fit);
      pool.push({ idea, fit, score: s + jitter(idea.id, a), reasons });
    }
    if (pool.length >= 26) break;
  }
  pool.sort((x, y) => y.score - x.score);
  // Diversity: don't let one subject area fill the list.
  const picked = [], perArea = {};
  for (const p of pool) {
    const area = p.idea.tags.interests[0];
    const cap = picked.length < 2 ? 1 : 5;
    if ((perArea[area] || 0) >= cap) continue;
    perArea[area] = (perArea[area] || 0) + 1;
    picked.push(p);
    if (picked.length === 22) break;
  }
  for (const p of pool) { if (picked.length >= 22) break; if (!picked.includes(p)) picked.push(p); }
  return { answers: a, top: picked.slice(0, 2), more: picked.slice(2, 22), pool: pool.length, relax: Math.min(relax, 2) };
}

function present(p) {
  const { quality, tags, ...copy } = p.idea;
  return {
    ...copy,
    fit: p.reasons.slice(0, 3).map((r) => r[1]),
    adapted: p.fit === 'adapt',
    facts: { agent_share: tags.agent_share, speed: tags.speed, budget: tags.budget, tech: tags.tech,
             customer: tags.customer, markets: tags.markets, channels: tags.channels, interests: tags.interests },
    checked: quality.verified,
  };
}

module.exports = { QUIZ, validate, rank, present };

if (require.main === module) {
  // CLI for the skill: node web/lib/match.js '<answers json>'
  const ideas = require('../data/ideas.json');
  const r = rank(ideas, JSON.parse(process.argv[2] || '{}'));
  console.log(JSON.stringify({ pool: r.pool, relax: r.relax, top: r.top.map(present), more: r.more.map(present) }, null, 2));
}
