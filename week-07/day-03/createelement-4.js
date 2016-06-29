var planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]


var parent = document.querySelector('.asteroids');
var child = parent.querySelector('li');
parent.removeChild(child);


for (i = 0; i < planetData.length; i++) {
  if (planetData[i]['asteroid']){
    newLi = document.createElement('Li');
    parent.appendChild(newLi);
    newLi.innerHTML = planetData[i]['content'];
    newLi.classList.add(planetData[i]['category'])}
  }
