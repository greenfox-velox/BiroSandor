'use strict';

readDom.buttonAdd.addEventListener('click', addNewTodo);
readDom.buttonDeleteDone.addEventListener('click', deleteOrDone);

function deleteOrDone (event) {
  if (event.target.classList.value === 'del-button'){
    delTodo(event, event.target.id)
  } else if (event.target.classList.value === 'done-button') {
    doneTodo(event, event.target.id)
  };
}

function onLoad () {
  readRequest.httpRequest ('GET', local, '', function (response){
    readDom.listTheTodos(response);
  });
}

function addNewTodo () {
  readRequest.httpRequest ('POST', local, JSON.stringify({text: input_text.value}), function (response) {
    readDom.createOneNewTodo(response);
    readDom.clear();
  });
}

function delTodo (event, id) {
  readRequest.httpRequest ('DELETE', local + '/' + id, JSON.stringify({destroyed: true}), function (response) {
    document.getElementById(id).remove();
  });
}

function doneTodo (event, id) {
  readRequest.httpRequest ('PUT', local + '/' + id, JSON.stringify({text: text, completed: true}),function () {
    event.target.classList.add('true');
  });
}

onLoad();
setInterval(readDom.reload, 10000);
