// Does cat have a cat class?
// If so, alert 'YEAH CAT!'
// If dolphin has a 'dolphin' class, replace apple's content with 'pear'
// If apple has an 'apple' class, replace cat's content with 'dog'
// Make apple red
// Make balloon less balloon-like

var divs = document.querySelectorAll('p');

divs.forEach(function(e) {
  if (e.textContent === 'cat' && e.classList.contains('cat')){
    alert('YEAH CAT!')
  }
})

var ap = document.querySelector('.apple');

divs.forEach(function(e) {
  if (e.textContent == 'dolphin' && e.classList.contains('dolphin')){
    ap.textContent = 'pear'
  }
})

var ca = document.querySelector('.cat')
divs.forEach(function(e) {
  if (e.textContent == 'apple' && e.classList.contains('apple')){
    ca.textContent = 'dog'
  }
})

ap.className = 'apple red';

var ball = document.querySelector('.balloon');
ball.classList.remove('balloon')
