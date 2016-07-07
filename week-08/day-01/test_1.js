'use strict';

var letterCounter = require('./1.js');
var tape = require('tape');

tape(function(t) {
  t.deepEqual(letterCounter.letterCounter('alma'), {a:2, l:1, m:1});
  t.end();
});
