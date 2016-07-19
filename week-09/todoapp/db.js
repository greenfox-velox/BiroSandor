'use strict';

var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'alma',
  database: 'todoapp'
});

con.connect();

module.exports = {
  readAll: readAll,
  readId: readId,
  createNewTodo: createNewTodo,
  updateTodo: updateTodo,
  deleteTodo: deleteTodo
}

function handleError (err) {
  if(err) {
    console.log(err.toString());
    return;
  }
}

function readAll (callback) {
    con.query('SELECT * FROM todos;', function(err,rows){
      handleError(err);
      callback(rows);
  });
}

function readId (id, callback){
  con.query('SELECT * FROM todos WHERE id = ?', id,function(err,rows){
    handleError(err);
    callback(rows);
  });
}

function createNewTodo(text, id, callback) {
  con.query("INSERT INTO todos (text) VALUES ('"+text+"')", id,function(err,rows){
    handleError(err);
    callback({id: rows.insertId, text: text})
  });
}

function updateTodo(id, completed, callback) {
  con.query('UPDATE todos SET completed = 1 WHERE id = ?', id, function(err,rows){
    handleError(err);
    callback({id: id, completed: true});
  });
}

function deleteTodo(id, callback) {
  con.query('DELETE FROM todos WHERE id = ?', id, function(err,rows){
    handleError();
    callback({id: id, destroyed: true});
  });
}
