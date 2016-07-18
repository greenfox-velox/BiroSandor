'use strict';
//Module pattern
// var dog = (function (){
//   var sound = 'woof';
//   return {
//     talk: function (){
//       console.log(sound);
//     }
//   }
// })();


// Revealing module pattern
var dog = (function (){
  var sound = 'woof';
  function publicTalk (){
    console.log(sound);
  }
  return {
    talk: publicTalk;
  }
})();

dog.talk();

//constructor pattern with prototype #1
// function Dog(sound){
//   this.sound = sound;
// }
//
// Dog.prototype.talk = function (){
//   console.log(this.sound);
// }
//
// var potyi = new Dog ('woof');
// potyi.talk();
//
// //constructor pattern with prototype #2
// function Dog () {
//  this.sound = 'woof';
// }
//
// Dog.prototype.talk = function () {
//  console.log(this.sound)
// }
//
// var sniffles = new Dog();
// sniffles.talk();
