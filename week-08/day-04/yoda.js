'use strict';

var button = document.querySelector('button');
button.addEventListener('click', submit);
var result = document.querySelector('p');

function submit () {
  var xhr = new XMLHttpRequest();
  var input_text = document.querySelector('.input_text');
  var text = input_text.value;
  var url = 'https://yoda.p.mashape.com/yoda?sentence=';
  var url_result = url + encodeURIComponent(text);
  xhr.open('GET', url_result);
  xhr.setRequestHeader("X-Mashape-Key", "ZSGWed9Jg2mshyGODAe61FHDfarrp1a5d19jsnn9hjyIPAwTyP");
  xhr.onreadystatechange = function() {
     if (xhr.readyState == 4) {
       result.textContent = xhr.response};
     };
xhr.send();
};
