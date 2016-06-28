'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 2, p: 2, l: 1}

function letterCounter(string) {
  var arr1 = string.split('');
  var result = {};

  arr1.forEach(function (e) {
    if (!(e in result)) {
      result[e] = 1;
    }else{
      result[e]++;
    }
  })
  return result;

}

console.log(letterCounter('alma'));
