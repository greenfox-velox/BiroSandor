// gather 10.000 candies! clicking the ‘Create candies’ button gives you 1 candy.
// you can buy a lollipop for 100 candies by clicking the ‘Buy lollipop’ button.
// 10 lollipops generate 1 candy per second.
'use strict';

var candyButton = document.querySelector('.candy-button');
var lollipopButton = document.querySelector('.lollipop-button');
var candyResult = document.querySelector('.candy p');
var lollipopResult = document.querySelector('.lollipop p');
var candyCounter = 0;
var lollipopCounter = 0;

candyButton.addEventListener('click', function() {increaseCandy()});
lollipopButton.addEventListener('click', function() {increaseLollipop(candyCounter);});

function setCandy () {
  candyResult.textContent = candyCounter;
};

function setLollipop () {
  lollipopResult.textContent = lollipopCounter;
};

function increaseCandy () {
  candyCounter++;
  setCandy ();
};

function increaseLollipop () {
  if (candyCounter >= 10) {
    candyCounter -= 10;
    lollipopCounter++;
    setCandy ();
    setLollipop();
};
};

setInterval(function() {
  if (lollipopCounter >= 10){
    candyCounter += Math.floor(lollipopCounter / 10);
    setCandy();
  }
  if (candyCounter === 10000){
    alert('Congratulation! You WIN!')
  };
}, 1000);
