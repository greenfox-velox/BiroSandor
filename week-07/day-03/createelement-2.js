// Remove the king from the list.
// Add 3 list items saying 'The Fox' to the list.

var parent = document.querySelector('.asteroids');
var child = parent.querySelector('li');
parent.removeChild(child);

newLi = document.createElement('Li');
parent.appendChild(newLi);
newLi.innerHTML = 'The Fox'

newLi = document.createElement('Li');
parent.appendChild(newLi);
newLi.innerHTML = 'The Fox'

newLi = document.createElement('Li');
parent.appendChild(newLi);
newLi.innerHTML = 'The Fox'
