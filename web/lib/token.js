// Signed, stateless codes. A visitor's quiz answers travel inside the code, so we never
// have to store "the other 20 ideas": they are recomputed from the answers when needed.
'use strict';
const crypto = require('crypto');

const DEV_SECRET = 'dev-only-secret-change-me';
function secret() {
  const s = process.env.QUIZ_SECRET;
  if (!s && process.env.VERCEL_ENV === 'production') throw new Error('QUIZ_SECRET is not set');
  return s || DEV_SECRET;
}
const b64 = (buf) => Buffer.from(buf).toString('base64url');
const mac = (body) => crypto.createHmac('sha256', secret()).update(body).digest('base64url').slice(0, 32);

function sign(payload) {
  const body = b64(JSON.stringify(payload));
  return `${body}.${mac(body)}`;
}

// Returns the payload, or null if the code is malformed, tampered with or expired.
function verify(token, maxAgeDays) {
  if (typeof token !== 'string' || token.length > 4000) return null;
  const [body, sig] = token.split('.');
  if (!body || !sig) return null;
  const want = mac(body);
  if (sig.length !== want.length || !crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(want))) return null;
  try {
    const p = JSON.parse(Buffer.from(body, 'base64url').toString('utf8'));
    if (maxAgeDays && (!p.t || Date.now() - p.t > maxAgeDays * 86400e3)) return null;
    return p;
  } catch { return null; }
}

module.exports = { sign, verify, usingDevSecret: () => !process.env.QUIZ_SECRET };
