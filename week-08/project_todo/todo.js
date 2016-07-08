'use strict';

var buttonAdd = document.querySelector('.button-text');
buttonAdd.addEventListener('click', addNewTodo);

var item = document.querySelector('ul');

function createOneNewTodo(todo) {
 var newItem = document.createElement('li');
 newItem.textContent = todo.text;
 newItem.setAttribute('id', todo.id);
 item.appendChild(newItem);
 createDelButton(newItem);
 createDoneButton(newItem, todo);
}

function createDelButton (parent) {
 var del = document.createElement('button');
 del.classList.add('del-button');
 del.setAttribute('id', parent.id);
 parent.appendChild(del);
 del.addEventListener('click', function(event){
   delTodo(event);
 });
}

function createDoneButton (parent, todo) {
 var done = document.createElement('button');
 if (todo.completed) {
  done.classList.add('true');
 } else {
  done.classList.add('done-button');
 }
 done.setAttribute('id', parent.id);
 parent.appendChild(done);
 done.addEventListener('click', function(event){
   doneTodo(event);
 });
}

function listTheTodos (todo) {
  todo.forEach(function (e) {
    createOneNewTodo(e);
  })};


function onLoad () {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.onreadystatechange = function() {
     if (xhr.readyState == 4) {
       var response = JSON.parse(xhr.response);
       listTheTodos(response)};
     };
  xhr.send();
};

onLoad();

function reload () {
  var container = document.querySelector('ul');
  container.innerHTML = '';
  onLoad();
};
setInterval(reload, 10000);

function addNewTodo () {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  var input_text = document.querySelector('.input_text');
  var text = input_text.value;
  var newTodo = JSON.stringify({text: text});
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
     if (xhr.readyState == 4) {
      var response = JSON.parse(xhr.response);
      createOneNewTodo(response);
     };
    };
  xhr.send(newTodo);
};

function delTodo (event) {
  var xhr = new XMLHttpRequest();
  var id = event.target.parentNode.id;
  xhr.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos' + '/' + id);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
     if (xhr.readyState == 4) {
      document.getElementById(id).remove();
     };
   };
   xhr.send();
};

function doneTodo (event) {
  var xhr = new XMLHttpRequest();
  var id = event.target.parentNode.id;
  var text = event.target.parentNode.textContent;
  var result = JSON.stringify({text: text, completed: true});
  xhr.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos' + '/' + id);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
      if (xhr.readyState == 4) {
        var response = JSON.parse(xhr.response);
        event.target.classList.add('true');
      }
    };
  xhr.send(result);
};
