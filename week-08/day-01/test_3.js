'use strict';

var rectangle = require('./3.js');
var tape = require('tape');

var firstTest = new rectangle.Rectangle(5,4);

tape(function(t) {
  t.deepEqual(firstTest.getArea(), 20);
  t.deepEqual(firstTest.getCircumference(), 18);
  t.deepEqual(firstTest.a, 5);
  t.deepEqual(firstTest.b, 4);
  t.end();
});
