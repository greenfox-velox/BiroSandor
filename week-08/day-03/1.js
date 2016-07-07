'use strict';

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count


var fs = require('fs');
function wordCount(filename, cb) {
  fs.readFile(filename, function(err, count) {
    if (err) {
      return cb(err);
    }
    var result = String(count).split(' ').length;
    cb(null, result);
  });
}

wordCount('alma.txt', function(err, c) {
  console.log(err, c);
});
