// fill output1 with the first paragraph's content, text only.
// fill output2 with the first paragraph's content keeping the cat strong.

var p1 = document.querySelector('p');
var o1 = document.querySelector('.output1');
var o2 = document.querySelector('.output2');

o1.textContent = p1.textContent;
o2.innerHTML = p1.innerHTML;
