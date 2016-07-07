'use strict';
//
var buttonAdd = document.querySelector('.button-text');
// var buttonDelete = document.querySelector('.function-button-delete');
// var buttonDone = document.querySelector('.function-button-done');
buttonAdd.addEventListener('click', addNewTodo);
// buttonDelete.addEventListener('click', deleteTodo);
// buttonDone.addEventListener('click', doneTodo);

function listTheTodos (todos) {
var item = document.querySelector('ul');

todos.forEach( function (e) {
  var newItem = document.createElement('li');
  item.appendChild(newItem);
  newItem.setAttribute('id', e['id']);
  newItem.textContent = e['text'];
})
};


function onLoad () {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.onreadystatechange = function() {
     if (xhr.readyState == 4) {
       var response = JSON.parse(xhr.response);
       listTheTodos(response);
       };
     };
  xhr.send();
};

onLoad();
// setinterval(onLoad, 10000);

function addNewTodo () {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  var input_text = document.querySelector('.input_text');
  var text = input_text.value;
  var newTodo = JSON.stringify({text: text});
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
     if (xhr.readyState == 4) {
      var item = document.querySelector('ul');
      var newItem = document.createElement('li');
      item.appendChild(newItem);
      newItem.textContent = text;
     };
     };
  xhr.send(newTodo);
};
//
// function deleteTodo () {
//
// };
//
// function doneTodo () {
//
// };
