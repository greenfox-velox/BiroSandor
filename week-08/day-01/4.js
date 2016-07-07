'use strict';

// Automated CarPark system
//
// All the dates in this examples should be stored as a number
// The milliseconds lasted from 1970-01-01
//
// Create a Car constructor
// it should take 3 parameters
//  - type: the cars type as a string (eg: 'volvo')
//  - color: the cars type as a string (eg: 'red')
//  - balance: the cars parking credis as a number (eg: 500)



function Car(type, color, balance) {
  this.type = type;
  this.color = color;
  this.balance = balance;
  this.enterDate = 0;
  this.id = Car.currentCarId++;
}

Car.currentCarId = 0;
//
// every car should have an id property (a number), that is
// unique for all the cars, staeting form 0
//
// Methods:
// enter(enterDate)

//  - it should store the date of entering
Car.prototype.enterDate = function (enterDate) {
  this.enterDate = enterDate;
  }


// getEnterDate()
//  - it should return the date of the last entering
Car.prototype.getEnterDate = function () {
  return this.enterDate;
};


// leave(price)
//  - it should decrease the balance with the price of the parking (that is given in an argument)

Car.prototype.leave = function (price) {
  this.balance -= price;
};


// getStats()
//  - it should give back a string like:
//    "Type: volvo, Color: red, Balance: 500"
Car.prototype.getStats = function () {
  return ('Type: ' + this.type + ', Color: ' + this.color + ', Balance: '+this.balance);
};

// Create a CarPark constructor
// it should take 2 parameters
//  - income: the initial credits as a number (eg: 4000)
//  - startTime: the current date
//
// The parking fee: 40 per hours (only every whole hour)
//
function CarPark (income, startTime) {
  this.income = income;
  this.startTime = startTime;
}

// Methods:
// carEnter(car)
//  - It should add a car to the garage and add its stored startTime
CarPark.prototype.carEnter = function (car) {
  this.car.push(car);
}

// carLeave(id)
//  - It should remove the car with the given id and it should charge from its balance
CarPark.prototype.carLeave = function (id) {
  this.cars = this.cars.filter(function(car) {
    
    return car.id !== id;
  })
}


// elapseTime(hours)
//  - It should increment the time with the hours
CarPark.prototype.elapseTime = function (hours) {
  this.hours += hours;
}


// Optional Methods:
//
// getStats()
//  - It should return a string like:
//    "Cars: 4, Time: 1234423453, Income: 1400"
//
// getParkingCarsSince(hours)
//  - It should return the number of cars that are parking since the given hours

var car1 = new Car('Ford', 'black', 500);
var car2 = new Car('Seat', 'yellow', 500);

console.log(car1.getStats());
console.log(car1.id);
console.log(car2.id);
