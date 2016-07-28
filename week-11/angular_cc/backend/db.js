'use strict';

function handleError (err) {
  if(err) {
    console.log(err.toString());
    return;
  }
}

var readTheFunctions = (function () {

  var mysql = require('mysql');

  var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'alma',
    database: 'meal',
    timezone: 'utc'
  });

  con.connect();


  function readAll (data, callback) {
    con.query('SELECT * FROM meals;', function(err,rows){
      handleError(err);
      callback(rows);
    });
  }

  function createNewMeal(req, callback) {
    con.query("INSERT INTO meals (meal, calories, date) VALUES ('"+ req.body.name +"','" +req.body.calories+ "', '"+req.body.date+"')", function(err,rows){
      handleError(err);
      callback({name: req.body.name, calories: req.body.calories, date: req.body.date})
    });
  }

  function deleteCalorie(id, callback) {
    con.query('DELETE FROM meals WHERE id = ?', id, function(err,rows){
      handleError();
      callback({id: id});
    });
  }

  return {
    readAll: readAll,
    createNewMeal: createNewMeal,
    deleteCalorie: deleteCalorie
  }
})();

module.exports = readTheFunctions;
