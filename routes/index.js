var express = require('express');
var router = express.Router();
const data = require('../data.json');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index.pug', {title:"Latest security news", data_list:data});
});

module.exports = router;
