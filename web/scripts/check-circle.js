// Read-only check of the Circle connection: looks one email up and prints what came back.
// Usage: CIRCLE_API_TOKEN=... node scripts/check-circle.js someone@example.com
'use strict';
const circle = require('../lib/circle');
(async () => {
  if (!circle.configured()) { console.error('Set CIRCLE_API_TOKEN first.'); process.exit(1); }
  const email = process.argv[2];
  if (!email) { console.error('Pass an email address that is already a member.'); process.exit(1); }
  try { console.log('search result:', JSON.stringify(await circle.findMember(email), null, 2)); }
  catch (e) { console.error(e.message, '\nIf this is 401, try CIRCLE_AUTH_SCHEME=Token.'); process.exit(1); }
})();
