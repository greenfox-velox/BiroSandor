'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements
var arr1 = [1,2,3]

//forEach
function each(func, arr) {
  arr.forEach(function(e) {func(e)});
}

//for loop
function each(func, arr) {
  for (var i = 0; i < arr.length; i++) {
    func(arr[i])};
}

each(console.log, arr1);
