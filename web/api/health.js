// GET /api/health -> which integrations are configured (never any secret values).
'use strict';
const ideas = require('../lib/library');
module.exports = (req, res) => res.status(200).json({
  ideas: ideas.length,
  circle: require('../lib/circle').configured() ? 'live' : 'dry_run',
  email: require('../lib/email').configured() ? 'live' : 'dry_run',
  secret: require('../lib/token').usingDevSecret() ? 'dev (set QUIZ_SECRET)' : 'set',
});
