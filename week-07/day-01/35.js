'use strict';

var ah = ['kuty', 'macsk', 'cic']
// add to all elements an 'a' on the end

for (var i = 0; i < ah.length; i++){
  console.log(ah[i]+= 'a');
}

var i = 0;
while (i < ah.length){
  console.log(ah[i]+='a');
  i++
}
