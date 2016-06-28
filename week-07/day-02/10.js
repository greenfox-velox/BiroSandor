'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  gradelist: [],
  addgrade: function(grade){
    this.gradelist.push(grade)},
  addAverage: function() {
    var totalgrade = 0;
    var l = this.gradelist.length
    for (var i = 0; i < l; i++) {
      totalgrade += this.gradelist[i]
    }
    var result = totalgrade / l;
    return result
  }
}

student.addgrade(1)
student.addgrade(5)
console.log(student.addAverage());
console.log(student);
