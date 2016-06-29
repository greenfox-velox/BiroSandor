function countTheListElement (){
  var summ = document.querySelectorAll('ul li');
  var getp = document.querySelector('.result');
  getp.textContent = summ.length
}



var button = document.querySelector('button');
button.addEventListener('click', countTheListElement)
