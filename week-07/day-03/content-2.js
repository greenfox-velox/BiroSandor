// fill every paragraph with the last one's content.

var allp = document.querySelectorAll('p');
var lastp = document.querySelector('.dog');

for (var i = 0; i < allp.length; i++) {
  allp[i].textContent = lastp.textContent;
}
