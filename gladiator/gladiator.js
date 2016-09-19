function something() {alert("WE DID SOMETHING!");}


var health = document.getElementById("health")
var attack = document.getElementById("attack")

function attack() { var attack = health.value - (Math.floor((Math.random() * 30) + 10));}
