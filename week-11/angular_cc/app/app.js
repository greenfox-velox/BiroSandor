var CalorieCounter = angular.module('CalorieCounter', ['ngAnimate']);

CalorieCounter.factory('Config', function() {
  return {
    baseUrl: 'http://localhost:3000'
  }
});

CalorieCounter.factory('CalorieService', function(Config, $http) {
  return {
    getAll: function() {
      return $http.get(Config.baseUrl + '/meals');
    },
  }
});



CalorieCounter.controller('AppController', ['$scope', '$http', function($scope, $http, CalorieService){

  $scope.addMeal = function () {
    $scope.meals.push({
      meal: $scope.newMeal.meal,
      calories: parseInt($scope.newMeal.calories),
      date: new Date($scope.newMeal.date)
    });

    $scope.newMeal.meal = "";
    $scope.newMeal.calories = "";
    $scope.newMeal.date = "";
  };

  $scope.deleteMeal = function (meal) {
    var toRemove = $scope.meals.indexOf(meal);
    $scope.meals.splice(toRemove, 1);
  };

  $scope.getCaloriesSum = function (meals, calories) {
    return meals.reduce(function (a, b) {
      return a + b[calories];
    }, 0);
  };

  $scope.reload = function(){
    $scope.search = "";
   };

  $scope.getSum = function(){
    var sum = 0;
    $scope.meals.forEach(function (meal) {
      sum += meal.calories;
    })
    return sum;
    }


  CalorieService.getAll().success(function(data) {
    $scope.meals = data;
    $scope.loading = false;
  }).finally;


  $http.get('./data/meals.json').success(function(data) {
    $scope.meals = data;
  });
}]);
