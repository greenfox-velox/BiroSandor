// 1. Alert the content of the header.
var headcontent = document.querySelector('h1');
alert(headcontent.innerHTML);

// 2. Write the content of the first paragraph to the console.
var firstp = document.querySelector('p');
console.log(firstp);

// 3. Alert the content of the second paragraph.
var secp = document.querySelector(':nth-child(3)');
alert(secp);
// 4. Replace the heading's content with 'New content'.
var heading = document.querySelector('h1');
heading.innerHTML = 'New content'
// 5. Replace the last paragraph's content with the first paragraph's content.
var par1 = document.querySelector('p');
var par2 = document.querySelector('.result');
par2.textContent = par1.textContent;
