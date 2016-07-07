'use strict';

// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error
var fs = require('fs');
function concatText(file1, file2, cb) {
  fs.readFile(file1, function(err, text1) {
    if (err) {
      return cb(err);
    }
    var result1 = String(text1);
    fs.readFile(file2, function(err, text2) {
      if (err) {
        return cb(err);
      }
    var result2 = String(text2);
    var result = result1.concat(result2);
    cb(err, result);
})})};


concatText('first.txt', 'second.txt', function(err, result) {
  console.log(err, result);
});
