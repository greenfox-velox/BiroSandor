'use strict';

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
var fs = require('fs');
function countLetter(fileName, letter, cb) {
  fs.readFile(fileName, function(err, count) {
    if (err) {
      return cb(err)
    }
    var readed = String(count).split('');
    var result = 0;
    readed.forEach(function(e) {
      if (e === letter) {
        result++;
      }
    });
    cb(null, result);
  });
}

countLetter('alma.txt', 'a', function(err, c) {
  console.log(err, c);
});
