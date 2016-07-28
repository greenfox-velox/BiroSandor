'use strict';

var db = require('./db.js');

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });


app.use(bodyParser.json());
app.use(express.static('../../angular_cc'));

app.get('/meals', function(req, res) {
  db.readAll(req, function(meal){
    res.send(meal)
  });
})

app.post('/meals', function(req, res){
  db.createNewMeal(req, function (meal){
    res.send(meal);
  });
})

app.delete('/meals/:id', function(req, res){
  db.deleteCalorie(req.params.id, function(meal){
    res.send(meal);
  });
})



app.listen(3000);
