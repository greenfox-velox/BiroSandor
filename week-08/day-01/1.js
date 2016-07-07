'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function letterCounter(string) {
  var arr1 = string.split('');
  var result = {};

  for (var i = 0; i < arr1.length; i++) {
    var item = arr1[i];
    result[item] = (result[item] + 1) || 1;
  }
  return result;
}

console.log(letterCounter('alma'));

module.exports.letterCounter = letterCounter;
