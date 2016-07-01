var imagelist = [
  {
    name: 'Family Guy',
    content: 'Family_Guy_Logo.svg.png'
  },
  {
    name: 'image1',
    content: 'images.png',
  },
  {
    name: 'image2',
    content: 'maxresdefault.png',
  },
  {
    name: 'image3',
    content: 'family-guy-bizarr-arcai-ernie-oriascsirke.png',
  },
  {
    name: 'image4',
    content: '437946-family-guy-family-guy-wallpaper.png'
  },
  {
    name: 'image5',
    content: '2454148-brianpbj.gif',
  },
  {
    name: 'image6',
    content: 'family-guy-peter-griffin7.png',
  },
  {
    name: 'image7',
    content: 'unnamed.png',
  },
]


var imagename = document.querySelector('h3');
imagename.textContent = 'Family Guy';

var imagesparent = document.querySelector('.pic');
var newimage1 = document.createElement('img');
imagesparent.appendChild(newimage1);
newimage1.setAttribute('src', 'Family_Guy_Logo.svg.png');

var list_of_images_js = document.querySelector('.list_of_images');
imagelist.forEach (function(e) {
var newimage = document.createElement('img');
list_of_images_js.appendChild(newimage);
newimage.setAttribute('src', e.content);
newimage.addEventListener('click', function(){newimage1.setAttribute('src', e.content);
imagename.textContent = e.name;}
    );
  }
);

var i = 0;
function getNewPic () {
  var picture = document.querySelector('.pic img');
  var name = document.querySelector('h3');
    picture.setAttribute('src', imagelist[i]['content']);
    name.textContent = imagelist[i]['name'];
}

function increaseIndex () {
  if (i < imagelist.length-1){
    i++;
  }else {i = 0;}
}

function decreasIndex () {
  if (i > 0){
    i--;
  }else {i = imagelist.length-1;}

var next = document.querySelector('.next.arrow');
next.addEventListener('click', function (){ increaseIndex(); getNewPic()});

var prev = document.querySelector('.prev.arrow');
prev.addEventListener('click', function (){ decreasIndex(); getNewPic()});
