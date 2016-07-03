var imagelist = [
  {
    name: 'Family Guy',
    content: 'images/Family_Guy_Logo.svg.png'
  },
  {
    name: 'image1',
    content: 'images/images.png',
  },
  {
    name: 'image2',
    content: 'images/maxresdefault.png',
  },
  {
    name: 'image3',
    content: 'images/family-guy-bizarr-arcai-ernie-oriascsirke.png',
  },
  {
    name: 'image4',
    content: 'images/437946-family-guy-family-guy-wallpaper.png'
  },
  {
    name: 'image5',
    content: 'images/2454148-brianpbj.gif',
  },
  {
    name: 'image6',
    content: 'images/family-guy-peter-griffin7.png',
  },
  {
    name: 'image7',
    content: 'images/unnamed.png',
  },
]

var imagename = document.querySelector('h3');
var imagesparent = document.querySelector('.picture');
var bigPicture = document.createElement('img');
var thumbnail = document.querySelector('.thumbnail');

imagename.textContent = 'Family Guy';


imagesparent.appendChild(bigPicture);
bigPicture.setAttribute('src', 'images/Family_Guy_Logo.svg.png');

for (var element = 0; element < 4; element++){
  var newimage = document.createElement('img');
  thumbnail.appendChild(newimage);
  newimage.setAttribute('src', imagelist[element].content);
  newimage.setAttribute('name', imagelist[element]['name']);
  getPicsSrc();
  if (newimage.src === bigPicture.src) {
    newimage.classList.add('current');
  } else {
    newimage.classList.remove('current');
  }
}

var mainPicStart = 0;
var thumbnailStart = 0;

function getPicsSrc (){
  var thumbnailPics = document.querySelectorAll('.thumbnail img');
  thumbnailPics.forEach(function(e, index) {
  e.addEventListener('click', function() {bigPicture.setAttribute('src', e.src);
  imagename.textContent = e.name; e.classList.add('current');
  if (newimage.src === bigPicture.src) {
    newimage.classList.add('current');
  } else {
    newimage.classList.remove('current');
  }

console.log(mainPicStart);
console.log(thumbnailStart);

  mainPicStart = index + thumbnailStart;})})}

var picture = document.querySelector('.picture img');
var name = document.querySelector('h3');
function getNewPic () {
  var name = document.querySelector('h3');
  picture.setAttribute('src', imagelist[mainPicStart]['content']);
  name.textContent = imagelist[mainPicStart]['name'];
  var current = document.querySelector('.current');
console.log(mainPicStart);
  if (mainPicStart > 3) {
    next1.style.display = 'none';
  }else{
    next1.style.display = 'block'
  }
}

function increaseIndex () {
  if (mainPicStart < imagelist.length-1){
    mainPicStart++;
  }else {mainPicStart = 0;}
}

function decreasIndex () {
  if (mainPicStart > 0){
    mainPicStart--;
  }else {mainPicStart = imagelist.length-1;}
}

function setName (element, newimage) {
  newimage.addEventListener('click', function(){bigPicture.setAttribute('src', imagelist[element].content)})
  newimage.setAttribute('src', imagelist[element]['content']);
  name.textContent = imagelist[element]['name'];

}

function slidePics () {
  for( var element =  thumbnailStart; element < thumbnailStart + 4; element++) {
  var newimage = document.createElement('img');
  thumbnail.appendChild(newimage);
  newimage.setAttribute('name', imagelist[element]['name']);
  newimage.setAttribute('src', imagelist[element].content); setName(element, newimage);
  if (thumbnailStart > 3) {
    next1.style.display = 'none';
  }else{
    next1.style.display = 'block'
  }
  if (thumbnailStart === 0){
    prev1.style.display = 'none';
  }else{
    prev1.style.display = 'block';
  }
  if (newimage.src === bigPicture.src) {
    newimage.classList.add('current');
  } else {
    newimage.classList.remove('current');
    }
  }
}

var thumbnailStart = 0;
function increaseIndexSlide () {
  if (thumbnailStart < imagelist.length-1){
    thumbnailStart++;
  }else {thumbnailStart = 0;
  }
}

function decreasIndexSlide () {
  if (thumbnailStart > 0){
    thumbnailStart--;
  }else {thumbnailStart = imagelist.length-1;}
}

var next = document.querySelector('.next.arrow');
next.addEventListener('click', function (){ increaseIndex(); getNewPic(); thumbnail.innerHTML = ''; increaseIndexSlide(); slidePics(); getPicsSrc()});
//
var prev = document.querySelector('.prev.arrow');
prev.addEventListener('click', function (){ decreasIndex(); getNewPic(); thumbnail.innerHTML = ''; decreasIndexSlide(); slidePics(); getPicsSrc()});
//
var next1 = document.querySelector('.next1.arrow');
next1.addEventListener('click', function(){thumbnail.innerHTML = ''; increaseIndexSlide(); slidePics(); getPicsSrc()});
//
var prev1 = document.querySelector('.prev1.arrow');
prev1.addEventListener('click', function() {thumbnail.innerHTML = ''; decreasIndexSlide(); slidePics(); getPicsSrc()});
