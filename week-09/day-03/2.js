// all books with its name, authors name, category name, publishers name and price

'use strict';

var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma',
  database: 'bookstore'
});

con.connect();

con.query('SELECT book_name, aut_name, cate_descrip, pub_name, book_price FROM book_mast JOIN author ON author.aut_id = book_mast.aut_id JOIN category ON category.cate_id = book_mast.cate_id JOIN publisher ON publisher.pub_id = book_mast.pub_id', function(err,rows){
  if(err) {
     console.log(err.toString());
       return;
   }
  console.log('Data received from Db:\n');
  var result = JSON.parse(JSON.stringify(rows));
  console.log(result);
});

con.end();
