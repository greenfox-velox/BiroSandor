// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.
var king = document.querySelector('.asteroid');
console.log(king);
// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.
var conceited = document.querySelector('.asteroid.b326');
alert(conceited);
// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.
var businessLamp = document.querySelectorAll('.big');
for (var i = 0; i < businessLamp.length; i++) {
  console.log(businessLamp[i]);
}
// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.
var conceitedKing = document.querySelectorAll('.container div');
for (var i = 0; i < conceitedKing.length; i++) {
  alert(conceitedKing[i]);
}
// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.
var noBusiness = document.querySelectorAll('div.asteroid');
for (var i = 0; i < noBusiness.length; i++) {
  console.log(noBusiness[i]);
}
// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.
var allBizniss = document.querySelector('p');
alert(allBizniss);
