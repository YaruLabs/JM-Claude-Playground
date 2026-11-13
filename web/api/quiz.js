// GET /api/quiz -> the quiz questions (single source: lib/quiz.json).
'use strict';
const quiz = require('../lib/quiz.json');
module.exports = (req, res) => { res.setHeader('Cache-Control', 'public, max-age=300'); res.status(200).json(quiz); };
