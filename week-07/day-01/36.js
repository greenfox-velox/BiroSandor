'use strict';

var ah = [3, 4, 5, 6, 7];
// print the sum of all numbers in ah
var total = 0;
for (var i = 0; i < ah.length; i++) {
  total += ah[i];
}
console.log(total);


var summ = 0;
var i = 0;
while (i < ah.length) {
  summ += ah[i];
  i++
}
console.log(summ);
