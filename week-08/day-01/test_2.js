'use strict';

var countBooks = require('./2.js');
var tape = require('tape');

tape(function(t) {
  t.deepEqual(countBooks.countBooks(countBooks.students), 4);
  t.end();
});
