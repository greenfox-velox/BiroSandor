// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']


var li = document.querySelectorAll('li');
var arr = ['apple', 'banana', 'cat', 'dog'];

for (var i = 0; i < li.length; i++) {
  li[i].textContent = arr[i]
}
