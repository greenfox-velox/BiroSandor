// Write the image's url to the console.
// Replace the image with a picture of yourself.
// Make the link point to the Green Fox Academy website.
// Disable the second button.
// Replace its text with 'Don't click me!'.

var imgurl = document.querySelector('img');
var pic = imgurl.getAttribute('src');
console.log(pic);

imgurl.setAttribute('src', 'https://avatars3.githubusercontent.com/u/17767814?v=3&s=460')

var linkto = document.querySelector('a');
linkto.getAttribute('href');
linkto.setAttribute('href','http://www.greenfoxacademy.com');

var disablebutton = document.querySelector('.this-one');
disablebutton.disabled = true;
disablebutton.textContent = 'Don\'t click me'
