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
   con.query('SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast JOIN author ON author.aut_id = book_mast.aut_id JOIN category ON category.cate_id = book_mast.cate_id JOIN publisher ON publisher.pub_id = book_mast.pub_id',function(err,rows){
     if(err) {
       console.log(err.toString());
       return;
     }
     res.send(rows);
   });
 });

app.listen(3000);
