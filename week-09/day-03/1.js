// all book names

'use strict';

var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma',
  database: 'bookstore'
});

con.connect();

// con.query('INSERT INTO todos (new_tablecol) VALUE ("buy milk")', function(err,rows){
//   if(err) {
//     console.log(err.toString());
//       return;
//   }
//   console.log(rows);
// });

con.query('SELECT book_name FROM book_mast;', function(err,rows){
  if(err) {
     console.log(err.toString());
       return;
   }
  console.log('Data received from Db:\n');
  var result = JSON.parse(JSON.stringify(rows));
  console.log(result);
});

con.end();
