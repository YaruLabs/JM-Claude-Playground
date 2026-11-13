// Shared rendering helpers. Everything is built with DOM nodes and textContent, never innerHTML.
'use strict';
function h(tag, attrs, ...kids) {
  const el = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs || {})) {
    if (v === false || v == null) continue;
    if (k === 'class') el.className = v; else if (k === 'text') el.textContent = v; else el.setAttribute(k, v === true ? '' : v);
  }
  for (const kid of kids.flat()) if (kid != null) el.append(kid);
  return el;
}

const AREA = { money: 'Money', health: 'Health', property: 'Property', food: 'Food', education: 'Education',
  travel_expat: 'Travel and expat life', ecommerce: 'Online selling', legal_paperwork: 'Paperwork and rules', pets: 'Pets',
  mobility: 'Transport', creator: 'Creators', local_services: 'Local services', work_careers: 'Careers', family_care: 'Family care' };
const MARKET = { TH_LOCAL: 'Thailand (Thai)', TH_EXPAT: 'Thailand (expats)', US: 'US', UK: 'UK and Europe', GLOBAL: 'Global' };
const BUDGET = { 1: 'Start under $100', 2: 'Start under $1,000', 3: 'Start under $5,000', 4: 'Needs $5,000+' };
const TECH = { none: 'No code needed', some: 'Some AI building', builder: 'Needs real engineering' };

function host(u) { try { return new URL(u).hostname.replace(/^www\./, ''); } catch { return null; } }

function ideaBody(i) {
  const f = i.facts;
  return [
    h('ul', { class: 'chips' },
      h('li', { text: `Agents run about ${f.agent_share}% (est.)` }),
      h('li', { text: `First customer in ${f.speed}` }),
      h('li', { text: BUDGET[f.budget] }),
      h('li', { text: TECH[f.tech] }),
      h('li', { text: f.markets.map((m) => MARKET[m]).join(', ') })),
    i.fit && i.fit.length ? h('div', { class: 'fit' }, h('h4', { text: 'Why this fits you' }), h('ul', {}, i.fit.map((t) => h('li', { text: t })))) : null,
    h('h4', { text: 'The problem' }), h('p', { text: i.problem }),
    h('h4', { text: 'Why it works' }), h('p', { text: i.why_it_works }),
    h('h4', { text: 'What AI agents do' }), h('ul', {}, i.agent_plan.map((t) => h('li', { text: t }))),
    h('h4', { text: 'What stays with you' }), h('p', { text: i.human_part }),
    h('h4', { text: 'Finding customers with content' }), h('p', { text: i.content_angle }),
    h('h4', { text: 'Your first three steps' }), h('ol', {}, i.first_steps.map((t) => h('li', { text: t }))),
    h('h4', { text: 'Pricing' }), h('p', { text: i.price_hint }),
    h('h4', { text: 'Watch out' }), h('p', { class: 'warn', text: i.watch_out }),
    i.competitors ? [h('h4', { text: 'Already in this space' }), h('p', { text: i.competitors })] : null,
    i.sources && i.sources.length ? [h('h4', { text: 'Sources' }), h('p', { class: 'srcs' },
      i.sources.filter(host).map((u) => h('a', { href: u, target: '_blank', rel: 'noopener noreferrer nofollow', text: host(u) })))] : null,
    h('p', { class: 'meta', text: `Last checked ${i.checked}. Figures marked "est." are estimates.` }),
  ].flat();
}

function ideaCard(i, n) {
  return h('article', { class: 'idea' },
    h('div', { class: 'tag', text: `Idea ${n} · ${AREA[i.facts.interests[0]] || ''}` }),
    h('h3', { text: i.name }), h('p', { class: 'one', text: i.one_liner }), ideaBody(i));
}

function ideaRow(i) {
  return h('details', { class: 'idea' },
    h('summary', {}, h('h3', { text: i.name }), h('span', { class: 'one', text: i.one_liner })), ideaBody(i));
}
