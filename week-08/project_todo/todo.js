'use strict';

var buttonAdd = document.querySelector('.button-text');
buttonAdd.addEventListener('click', addNewTodo);

var item = document.querySelector('ul');

// var url = 'https://mysterious-dusk-8248.herokuapp.com/todos'
var local = 'http://localhost:3000/todos'
var input_text = document.querySelector('.input_text');

function httpRequest (method, url, data, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, url);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(data);
  xhr.onload = function() {
  if (xhr.readyState === xhr.DONE) {
    var response = JSON.parse(xhr.response);
    callback(response)};
  };
}

function onLoad () {
  httpRequest ('GET', local, '', function (response){
    listTheTodos(response);
  });
}

function addNewTodo () {
  httpRequest ('POST', local, JSON.stringify({text: input_text.value}), function (response) {
    createOneNewTodo(response);
    clear();
  });
}

function delTodo (event) {
  var id = event.target.parentNode.id;
  httpRequest ('DELETE', local + '/' + id, JSON.stringify({destroyed: true}), function (response) {
    document.getElementById(id).remove();
  });
}

function doneTodo (event) {
  var id = event.target.parentNode.id;
  httpRequest ('PUT', local + '/' + id, JSON.stringify({text: text, completed: true}),function () {
    event.target.classList.add('true');
  });
}

function listTheTodos (todo) {
  todo.forEach(function (e) {
    createOneNewTodo(e);
  });
}

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

function reload () {
  var container = document.querySelector('ul');
  container.innerHTML = '';
  onLoad();
};

setInterval(reload, 10000);

function clear() {
  var content = document.querySelector('.input_text');
  content.value = '';
}

onLoad();
