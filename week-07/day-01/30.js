'use strict';

var ac = 8;
var time = 120;
var out = '';
// if ac is dividable by 4
// and time is not more than 200
// set out to 'check'
// if time is more than 200
// set out to 'Time out'
// otherwise set out to 'Run Forest Run!'

if (time > 200) {
  console.log('Time out!');
} else if (ac % 4 === 0) {
  console.log('check!');
} else {
  console.log('Run Forest Run!');
}
