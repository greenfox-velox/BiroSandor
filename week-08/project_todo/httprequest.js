'use strict';

var local = 'http://localhost:3000/todos'
var readRequest = (function () {
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
  return {
    httpRequest: httpRequest
  }
}) ();
