'use strict';

var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

app.use(bodyParser.json());
app.use(express.static('../../week-08/project_todo'));

var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma',
  database: 'todoapp'
});

con.connect();

app.get('/todos', function(req, res) {
  con.query('SELECT * FROM todos;', function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
  res.send(rows);
  });
})


app.get('/todos/:id', function(req, res){
  con.query('SELECT * FROM todos WHERE id = ?', req.params.id,function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
  res.send(JSON.parse(JSON.stringify(rows)));
})})

app.post('/todos', function(req, res){
  con.query("INSERT INTO todos (text) VALUES ('"+req.body.text+"')", req.params.id,function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
  res.send({id: rows.insertId, text: req.body.text});
})})

app.put('/todos/:id', function(req, res){
  con.query('UPDATE todos SET completed = 1 WHERE id = ?', req.params.id, function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
  res.send({id: req.params.id, completed: true});
})})

app.delete('/todos/:id', function(req, res){
  con.query('DELETE FROM todos WHERE id = ?', req.params.id, function(err,rows){
    if(err) {
      console.log(err.toString());
      return;
    }
  res.send({destroyed: true});
})})

// app.get('/todos', function(req, res){
//   con.query('SELECT * FROM todos WHERE completed = 1', function(err,rows){
//     if(err) {
//       console.log(err.toString());
//       return;
//     }
//   res.send(JSON.parse(JSON.stringify(rows)));
// })})

app.listen(3000);
