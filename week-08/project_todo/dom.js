'use strict';

var readDom = (function (){
  var input_text = document.querySelector('.input_text');
  var buttonAdd = document.querySelector('.button-text');
  var buttonDeleteDone = document.querySelector('ul');
  var item = document.querySelector('ul');

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
  }

  function reload () {
    var container = document.querySelector('ul');
    container.innerHTML = '';
    onLoad();
  };

  function clear() {
    var content = document.querySelector('.input_text');
    content.value = '';
  }

  return {
    listTheTodos: listTheTodos,
    createOneNewTodo: createOneNewTodo,
    createDelButton: createDelButton,
    createDoneButton: createDoneButton,
    reload: reload,
    clear: clear,
    buttonAdd: buttonAdd,
    buttonDeleteDone: buttonDeleteDone
  }
}) ();
