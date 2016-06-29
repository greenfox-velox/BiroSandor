'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack() {
  this.elementsList = [];
  this.elementsNumber = 0;
  this.size = function () {
    return this.elementsNumber;
  }

  this.push = function(element) {
    this.elementsList[this.elementsNumber] = element;
    this.elementsNumber ++;
  }

  this.pop = function() {
    this.elementsNumber --;
    for (var i = 0; i < this.elementsNumber; i++) {
      this.elementsList[this.elementsNumber]  = this.elementsList[this.elementsNumber];
    }
    return this.elementsList;
  }
}

var test1 = new Stack();
test1.push(2);
test1.push(3);
test1.pop()
console.log(test1);

console.log(test1.size());
