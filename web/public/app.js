// Landing -> quiz -> results -> join. Quiz questions come from /api/quiz (same file the matcher uses).
'use strict';
const $ = (id) => document.getElementById(id);
const store = {
  get(k) { try { return JSON.parse(localStorage.getItem(k)); } catch { return null; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* private mode */ } },
  del(k) { try { localStorage.removeItem(k); } catch { /* private mode */ } },
};
let QUIZ = null, step = 0, answers = {}, token = null;

function show(id) {
  for (const v of ['landing', 'quiz', 'results']) $(v).hidden = v !== id;
  window.scrollTo(0, 0);
}

async function api(path, body) {
  const res = await fetch(path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || 'Something went wrong. Please try again.');
  return data;
}

function renderQuestion() {
  const q = QUIZ.questions[step], total = QUIZ.questions.length;
  $('count').textContent = `Question ${step + 1} of ${total}`;
  $('left').textContent = step === total - 1 ? 'Last one' : `${total - step - 1} to go`;
  $('bar').setAttribute("aria-valuenow", step + 1);
  $('bar').setAttribute('aria-valuemax', total);
  $('bar').firstElementChild.style.width = `${((step + 1) / total) * 100}%`;
  $('back').style.visibility = step === 0 ? 'hidden' : 'visible';
  const multi = q.type === 'multi';
  const chosen = () => (multi ? answers[q.id] || [] : answers[q.id]);
  const opts = h('div', { class: 'opts' + (q.options.length > 6 ? ' grid2' : ''), role: 'group', 'aria-label': q.title },
    q.options.map((o) => {
      const on = multi ? chosen().includes(o.id) : chosen() === o.id;
      const b = h('button', { class: 'opt', type: 'button', 'aria-pressed': String(on) }, o.label, o.note ? h('small', { text: o.note }) : null);
      b.addEventListener('click', () => {
        if (multi) {
          const cur = new Set(chosen());
          if (cur.has(o.id)) cur.delete(o.id); else if (cur.size < q.max) cur.add(o.id);
          answers[q.id] = [...cur];
          renderQuestion();
        } else {
          answers[q.id] = o.id;
          store.set('quiz_answers', answers);
          advance();
        }
      });
      return b;
    }));
  $('q').replaceChildren(h('h2', { text: q.title }), q.help ? h('p', { class: 'help', text: q.help }) : null, opts);
  const next = $('next');
  next.hidden = !multi;
  next.disabled = multi && !chosen().length;
  next.textContent = step === total - 1 ? 'See my ideas' : 'Next';
  store.set('quiz_answers', answers);
}

async function advance() {
  if (step < QUIZ.questions.length - 1) { step++; renderQuestion(); return; }
  $('q').replaceChildren(h('h2', { text: 'Matching you to the library…' }));
  $('next').hidden = true;
  $('bar').firstElementChild.style.width = '100%';
  try { showResults(await api('/api/match', { answers })); }
  catch (e) { $('q').replaceChildren(h('h2', { text: 'That did not work' }), h('p', { class: 'help', text: e.message })); }
}

function showResults(r) {
  token = r.token;
  store.set('quiz_token', token);
  history.replaceState(null, '', '#r=' + token);
  $('libsize').textContent = r.library_size;
  $('ideas').replaceChildren(...r.ideas.map((i, n) => ideaCard(i, n + 1)));
  const shown = r.more.slice(0, 8);
  $('teasers').replaceChildren(...shown.map((m) => h('li', { text: m.name })),
    r.more.length > shown.length ? h('li', { text: `+ ${r.more.length - shown.length} more` }) : null);
  $('join-form').hidden = false;
  $('join-done').hidden = true;
  show('results');
}

function startQuiz() {
  answers = store.get('quiz_answers') || {};
  step = 0;
  show('quiz');
  renderQuestion();
}

$('form').addEventListener('submit', async (ev) => {
  ev.preventDefault();
  const f = ev.target, msg = $('msg');
  msg.className = 'msg';
  if (!f.email.value.includes('@')) { msg.className = 'msg err'; msg.textContent = 'Enter your email address.'; f.email.focus(); return; }
  if (!f.consent.checked) { msg.className = 'msg err'; msg.textContent = 'Please tick the box to join.'; return; }
  $('submit').disabled = true;
  msg.textContent = 'Sending…';
  try {
    const r = await api('/api/join', { email: f.email.value, name: f.name.value, website: f.website.value, consent: true, token });
    $('join-form').hidden = true;
    $('join-done').hidden = false;
    if (r.dev_link) {
      $('devlink').hidden = false;
      $('devlink').replaceChildren('Test mode (no email provider set): ', h('a', { href: r.dev_link, text: 'open your ideas', style: 'color:#ffb3bb' }));
    }
    $('join-done').scrollIntoView({ block: 'center' });
  } catch (e) {
    msg.className = 'msg err';
    msg.textContent = e.message;
  } finally { $('submit').disabled = false; }
});

document.querySelectorAll('[data-start]').forEach((b) => b.addEventListener('click', startQuiz));
$('back').addEventListener('click', () => { if (step > 0) { step--; renderQuestion(); } });
$('next').addEventListener('click', advance);
$('retake').addEventListener('click', () => { store.del('quiz_answers'); store.del('quiz_token'); history.replaceState(null, '', location.pathname); answers = {}; startQuiz(); });

(async function init() {
  QUIZ = await (await fetch('/api/quiz')).json();
  // A returning visitor (saved code or a results link) goes straight back to their ideas.
  const saved = (location.hash.match(/^#r=(.+)$/) || [])[1] || store.get('quiz_token');
  if (saved) {
    try { showResults(await api('/api/match', { token: saved })); } catch { store.del('quiz_token'); history.replaceState(null, '', location.pathname); }
  }
})();
