function addClassName () {
  var newClass = document.querySelector('div');
  newClass.classList.toggle('party')
}

var button = document.querySelector('button');

button.addEventListener('click', addClassName)
