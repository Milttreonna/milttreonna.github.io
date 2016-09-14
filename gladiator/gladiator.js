function something() {alert("WE DID SOMETHING!");}


var other= function (health) {health=100}
var self = function (health) {health=100}
var showHealth=document.getElementById("health");

var lowdamage= Math.floor((Math.random() * 20) + 11);
var highdamage= Math.floor((Math.random() * 30) + 21);

# when one player presses attack button, the others health should go down
var attack = function (self, other) {
  myAttack= document.getElementById('attack');

  var hit=(Math.random()* self.lowdamage, + self.highdamage));
  if (hit > 20) {
    hit *= 2 ; alert("RAGE!");
  }
  else {hit};
  other.health =+ hit
}
