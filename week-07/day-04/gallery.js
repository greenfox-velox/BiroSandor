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
imagelist.forEach (function(e, index) {
var newimage = document.createElement('img');
list_of_images_js.appendChild(newimage);
newimage.setAttribute('src', e.content);
newimage.addEventListener('click', function(){newimage1.setAttribute('src', e.content);
imagename.textContent = e.name;
i = index+j;

}
    );
  }
);
var picture = document.querySelector('.pic img');
var name = document.querySelector('h3');

var i = 0;
function getNewPic () {
    var name = document.querySelector('h3');
    picture.setAttribute('src', imagelist[i]['content']);
    name.textContent = imagelist[i]['name'];
    var current = document.querySelector('.current');

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
}

function getPicsSrc (){
  var thumbnailPics = document.querySelectorAll('.list_of_images img');
    thumbnailPics.forEach(function(e, index) {
    e.addEventListener('click', function() {newimage1.setAttribute('src', e.src);
    imagename.textContent = e.name;
    i = index+j;
  });
  })
}

function setName (element, newimage) {
  newimage.addEventListener('click', function(){newimage1.setAttribute('src', imagelist[element].content); })
  newimage.setAttribute('src', imagelist[element]['content']);
  name.textContent = imagelist[element]['name'];

}

function slidePics () {
  for( var element =  j; element < j + 4; element++) {
  var newimage = document.createElement('img');
  list_of_images_js.appendChild(newimage);
  newimage.setAttribute('name', imagelist[element]['name']);
  newimage.setAttribute('src', imagelist[element].content); setName(element, newimage);
  if (j === 4) {
    next1.style.display = 'none';
  }else{
    next1.style.display = 'block'
  }
  if (j === 0){
    prev1.style.display = 'none';
  }else{
    prev1.style.display = 'block';
  }


  }
}

var j = 0;
function increaseIndexSlide () {
  if (j < imagelist.length-1){
    j++;
  }else {j = 0;
  }
}

function decreasIndexSlide () {
  if (j > 0){
    j--;
  }else {j = imagelist.length-1;}
}

var next = document.querySelector('.next.arrow');
next.addEventListener('click', function (){ increaseIndex(); getNewPic()});

var prev = document.querySelector('.prev.arrow');
prev.addEventListener('click', function (){ decreasIndex(); getNewPic()});

var next1 = document.querySelector('.next1.arrow');
next1.addEventListener('click', function(){list_of_images_js.innerHTML = ''; increaseIndexSlide(); slidePics(); getPicsSrc()});
//
var prev1 = document.querySelector('.prev1.arrow');
prev1.addEventListener('click', function() {list_of_images_js.innerHTML = ''; decreasIndexSlide(); slidePics(); getPicsSrc()});
