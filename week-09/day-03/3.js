'use strict';

var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma',
  database: 'bookstore'
});

con.connect();

var express = require('express');
var app = express();

app.get('/', function(req, res) {
   con.query('SELECT book_name FROM book_mast;',function(err,rows){
     if(err) {
       console.log(err.toString());
       return;
     }
     res.send(rows);
   });
 });

app.listen(3000);
