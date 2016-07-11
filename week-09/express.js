var express = require('express');
var app = express();

app.get('*', function(req, res) {

  var date = new Date();
  res.send(req.path + ' ' + req.method+ ' ' + date);
})

app.listen(3000);
