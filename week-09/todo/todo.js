var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({ extended: false });

app.use(bodyParser.json());
app.use(express.static('../../week-08/project_todo'));

var list = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }
]

var id = 3;


app.get('/todos', function(req, res) {
  res.send(list);
})


function checkId (selectedId) {
  for (var i = 0; i < list.length; i++){
    if (parseInt(list[i].id) === parseInt(selectedId)){
      return list[i]
    }
  }
}

app.get('/todos/:id', function(req, res){
  res.send(checkId(req.params.id));
});

function addNewTodo (newText) {
  var text = newText;
  id++;
  var newTodo = {"completed": false, "id": id, "text": text};
  list.push(newTodo);
  return newTodo;
}

app.post('/todos', urlencodedParser, function(req, res){
  res.send(addNewTodo(req.body.text));
})

function changeCompleted (selectedId, newText) {
  for (var i = 0; i < list.length; i++){
    if (parseInt(list[i].id) === parseInt(selectedId)){
      list[i].completed = true;
      list[i].text = newText;
      return list[i];
    }
  }
}

app.put('/todos/:id', function(req, res){
  res.send(changeCompleted(req.params.id, req.body.text));
})

function removeElement (selectedId) {
  for (var i = 0; i < list.length; i++){
    if (parseInt(list[i].id) === parseInt(selectedId)){
      list[i].destroyed = true;
      return list.splice(i, 1)[0];
    }
  }
}

app.delete('/todos/:id', function(req, res){
  if (checkId(req.params.id)){
      res.send(removeElement(req.params.id));
  } else {
    res.sendStatus(404);
  }

})

app.listen(3000);
