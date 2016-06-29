// Add an item that says 'The Green Fox' to the asteroid list.
// Add an item that says 'The Lamplighter' to the asteroid list.
// Add a heading saying 'I can add elements to the DOM!' to the .container.
// Add an image, any image, to the container.


var list1 = document.querySelector('.asteroids');
newLi = document.createElement('Li');
list1.appendChild(newLi);
newLi.innerHTML = 'The Green Fox'
newLi = document.createElement('Li');
list1.appendChild(newLi);
newLi.innerHTML = 'The Lamplighter'

newH = document.createElement('h1');
var cont = document.querySelector('.container');
cont.appendChild(newH);
newH.innerHTML = 'I can add elements to the DOM!'

newpic = document.createElement('img');
cont.appendChild(newpic);
newpic.setAttribute('src', 'https://static.wixstatic.com/media/f4461b_83457ca5dd844c71a760d36e6583d0ff.png/v1/fill/w_168,h_168,al_c,usm_0.66_1.00_0.01/f4461b_83457ca5dd844c71a760d36e6583d0ff.png')
