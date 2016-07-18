

window.addEventListener('keypress', buttonPressed);

function buttonPressed() {
    var keyPressed = event.keyCode || event.which;
    if(keyPressed==105) {
      onIPress();
      keyPressed=null;
    } else if (keyPressed == 104) {
      onHPress();
      keyPressed=null;
    }else if (keyPressed==100) {
      onDPress();
      keyPressed=null;
    }else if (keyPressed==97) {
      onAPress();
      keyPressed=null;
    }else if (keyPressed==112) {
      onPPress();
      keyPressed=null;
    }
}


var images = document.querySelectorAll('img');
var headers = document.querySelectorAll('h1');
var containers = document.querySelectorAll('div');
var links = document.querySelectorAll('a');
var paragraphs = document.querySelectorAll('p');

var i = 0;
var h = 0;
var d = 0;
var a = 0;
var p = 0;

function onIPress () {
  images[i].setAttribute('src', "http://i254.photobucket.com/albums/hh114/inphact/000.gif");
  setTimeout(function () {images[i].setAttribute('src', ''); i++;},1000)
}

function onHPress () {
  headers[h].innerHTML = '<img src="http://i254.photobucket.com/albums/hh114/inphact/000.gif">';
  setTimeout(function () {headers[h].innerHTML = ''; h++;},1000)
}

function onDPress () {
  containers[d].innerHTML = '<img src="http://i254.photobucket.com/albums/hh114/inphact/000.gif">';
  setTimeout(function () {containers[d].innerHTML = ''; d++;},1000)
}

function onAPress () {
  links[a].innerHTML = '<img src="http://i254.photobucket.com/albums/hh114/inphact/000.gif">';
  setTimeout(function () {links[a].innerHTML = ''; a++;},1000)
}

function onPPress () {
  paragraphs[p].innerHTML = '<img src="http://i254.photobucket.com/albums/hh114/inphact/000.gif">';
  setTimeout(function () {paragraphs[p].innerHTML = ''; p++;},1000)
}

alert('Distroy function is activated! Press "i" to destroy images, "h" to headers, "d" to divs, "a" to links, "p" to the paragraphs');
