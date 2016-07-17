'use strict';

var db = require('./db.js');
var db_mongo = require('./db_mongo.js')

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

app.use(bodyParser.json());
app.use(express.static('../../week-08/project_todo'));

app.get('/todos', function(req, res) {
  db.readAll(req, function (todo){
      res.send(todo)
    });
})

app.get('/todos/:id', function(req, res){
  db.readId(req.params.id, function (todo){
    res.send(todo);
  });
})

app.post('/todos', function(req, res){
  db.createNewTodo(req, function (todo){
    res.send(todo);
  });
})

app.put('/todos/:id', function(req, res){
  db.updateTodo(req.params.id, req.body.completed, function (todo) {
    res.send(todo);
  });
})

app.delete('/todos/:id', function(req, res){
    db.deleteTodo(req.params.id, function(todo){
      res.send(todo);
    });
})

app.listen(3000);
