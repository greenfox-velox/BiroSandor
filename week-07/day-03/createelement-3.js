// Remove the king from the list.
// Add list items that have the following text contents:
var arr =['apple', 'bubble', 'cat', 'green fox']

var parent = document.querySelector('.asteroids');
var child = parent.querySelector('li');
parent.removeChild(child);

for (i = 0; i < arr.length; i++) {
newLi = document.createElement('Li');
parent.appendChild(newLi);
newLi.innerHTML = arr[i]}

// forEach
// var parent = document.querySelector('.asteroids');
// var child = parent.querySelector('li');
// parent.removeChild(child);
//
//
// var elementList = ['apple', 'bubble', 'cat', 'green fox'];
// elementList.forEach(function (e) {
//  var newLi = document.createElement('li');
//  newLi.textContent = e;
//  parent.appendChild(newLi);
// });
