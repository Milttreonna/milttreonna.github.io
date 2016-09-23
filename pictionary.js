window.onload = function () {

  var alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z'];

  var puzzlename;
  var thepuzzle;
  var word ;
  var guess ;
  var guesses = [ ];
  var lives ;
  var counter ;
  var space;



  var buttons = function () {
    myButtons = document.getElementById('buttons');
    letters = document.createElement('ul');

    for (var i = 0; i < alphabet.length; i++) {
      letters.id = 'alphabet';
      list = document.createElement('li');
      list.id = 'letter';
      list.innerHTML = alphabet[i];
      check();
      myButtons.appendChild(letters);
      letters.appendChild(list);
    }
  }

var showCatagory = document.getElementById("scatagory");
var image1 = document.getElementById("puzzimage1")
var image2 = document.getElementById("puzzimage2")
var image3 = document.getElementById("puzzimage3")
var image4 = document.getElementById("puzzimage4")

  var selectCat = function () {
    if (thepuzzle === puzzlename[0]) {
      image1.src = "doll1.jpg"
      image2.src = "doll2.jpg"
      image3.src = "doll3.jpg"
      image4.src = "doll4.jpg"
      catagoryName.innerHTML = "Puzzle 1";
    } else if (thepuzzle === puzzlename[1]) {
      image1.src = "trell.jpg"
      image2.src = "trell1.gif"
      image3.src = "trell1.png"
      image4.src = "trell2.jpg"
      catagoryName.innerHTML = "Puzzle 2";
    } else if (thepuzzle === puzzlename[2]) {
      image1.src = "mcneece.jpg"
      image2.src = "mcneece1.jpg"
      image3.src = "mcneece2.png"
      image4.src = "mcneece4.jpg"

      catagoryName.innerHTML = "Puzzle 3";
    }
    else if (thepuzzle === puzzlename[3]) {
      image1.src = "ramirez.jpg"
      image2.src = "ramirez1.jpg"
      image3.src = "ramirez2.gif"
      image4.src = "ramirez3.jpg"
      var audio = new Audio('salsa.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 4";
    }
    else if (thepuzzle === puzzlename[4]) {
      image1.src = "chris.jpg"
      image2.src = "chris1.jpg"
      image3.src = "chris2.png"
      image4.src = "chris3.jpg"
      var audio = new Audio('truck.mp3');
audio.play();

      catagoryName.innerHTML = "Puzzle 5";
    }
    else if (thepuzzle === puzzlename[5]) {
      image1.src = "sam.png"
      image2.src = "sam1.jpg"
      image3.src = "sam2.jpg"
      image4.src = "sam3.jpg"
      var audio = new Audio('horse.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 6";
    }
    else if (thepuzzle === puzzlename[6]) {
      image1.src = "mary.jpg"
      image2.src = "mary1.jpg"
      image3.src = "mary2.jpg"
      image4.src = "mary3.jpg"
      catagoryName.innerHTML = "Puzzle 7";
    }
    else if (thepuzzle === puzzlename[7]) {
      image1.src = "kira.jpg"
      image2.src = "kira1.jpg"
      image3.src = "kira2.jpg"
      image4.src = "kira3.jpg"
      catagoryName.innerHTML = "Puzzle 8";
    }

    else if (thepuzzle === puzzlename[8]) {
      image1.src = "chase.gif"
      image2.src = "chase1.jpg"
      image3.src = "chase2.jpg"
      image4.src = "chase3.jpg"
      catagoryName.innerHTML = "Puzzle 9";
    }
    else if (thepuzzle === puzzlename[9]) {
      image1.src = "porky.jpg"
      image2.src = "porkey1.jpg"
      image3.src = "porkey2.jpg"
      image4.src = "white.png"
      var audio = new Audio('pig.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 10";
    }
    else if (thepuzzle === puzzlename[10]) {
      image1.src = "pokey.jpg"
      image2.src = "pokey1.png"
      image3.src = "pokey2.jpg"
      image4.src = "white.png"
      var audio = new Audio('poke.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 11";
    }
    else if (thepuzzle === puzzlename[11]) {
      image1.src = "black.jpg"
      image2.src = "black1.jpg"
      image3.src = "black2.jpg"
      image4.src = "black3.png"
      var audio = new Audio('bang.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 12";
    }

    else if (thepuzzle === puzzlename[12]) {
      image1.src = "byrd.jpg"
      image2.src = "byrd1.jpg"
      image3.src = "byrd2.jpg"
      image4.src = "byrd3.jpg"
      var audio = new Audio('Eagle.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 13";
    }

    else if (thepuzzle === puzzlename[13]) {
      image1.src = "anderson.jpg"
      image2.src = "anderson1.png"
      image3.src = "anderson2.png"
      image4.src = "anderson3.jpg"
      var audio = new Audio('laugh.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 14";
    }
    else if (thepuzzle === puzzlename[14]) {
      image1.src = "clouse.jpg"
      image2.src = "clouse1.jpg"
      image3.src = "clouse2.jpg"
      image4.src = "clouse3.jpg"
      var audio = new Audio('clouse.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 15";
    }
    else if (thepuzzle === puzzlename[15]) {
      image1.src = "chey.jpg"
      image2.src = "chey1.jpg"
      image3.src = "chey2.jpg"
      image4.src = "white.png"
      var audio = new Audio('eating.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 16";
    }

    else if (thepuzzle === puzzlename[16]) {
      image1.src = "beasty.png"
      image2.src = "beasty1.jpg"
      image3.src = "beasty2.jpg"
      image4.src = "beasty3.jpg"
      catagoryName.innerHTML = "Puzzle 17";
    }


    else if (thepuzzle === puzzlename[17]) {
      image1.src = "bri.jpg"
      image2.src = "white.png"
      image3.src = "white.png"
      image4.src = "white.png"
      var audio = new Audio('monkey.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 18";
    }

    else if (thepuzzle === puzzlename[18]) {
      image1.src = "terious.jpg"
      image2.src = "terious1.jpg"
      image3.src = "terious2.png"
      image4.src = "white.png"
      var audio = new Audio('crying.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 19";
    }
    else if (thepuzzle === puzzlename[19]) {
      image1.src = "clayton.jpg"
      image2.src = "clayton1.jpg"
      image3.src = "clayton2.jpg"
      image4.src = "white.png"
      catagoryName.innerHTML = "Puzzle 20";
    }

    else if (thepuzzle === puzzlename[20]) {
      image1.src = "mira.png"
      image2.src = "mira1.jpg"
      image3.src = "mira2.jpg"
      image4.src = "mira3.jpg"
      var audio = new Audio('car.mp3');
audio.play();
      catagoryName.innerHTML = "Puzzle 21";
    }
  }


   result = function () {
    words = document.getElementById('hold');
    correct = document.createElement('ul');

    for (var i = 0; i < word.length; i++) {
      correct.setAttribute('id', 'my-word');
      guess = document.createElement('li');
      guess.setAttribute('class', 'guess');
      if (word[i] === "-") {
        guess.innerHTML = "-";
        space = 1;
      } else {
        guess.innerHTML = "_";
      }

      guesses.push(guess);
      words.appendChild(correct);
      correct.appendChild(guess);
    }
  }

var showLives = document.getElementById("mylives");
   comments = function () {
    showLives.innerHTML = "You have " + lives + " more tries.";
    if (lives < 1) {
      showLives.innerHTML = "Game Over";
    }
    for (var i = 0; i < guesses.length; i++) {
      if (counter + space === guesses.length) {
        showLives.innerHTML = "You Win!";
      }
    }
  }

   check = function () {
    list.onclick = function () {
      var guessone = (this.innerHTML);
      this.setAttribute("class", "active");
      this.onclick = null;
      for (var i = 0; i < word.length; i++) {
        if (word[i] === guessone) {
          guesses[i].innerHTML = guessone;
          counter += 1;
        }
      }
      var j = (word.indexOf(guessone));
      if (j === -1) {
        lives -= 1;
        comments();
      } else {
        comments();
      }
    }
  }

  play = function () {
    puzzlename = [
         ["doll"], ["kentrell"], ["mr mcneece"],["mr ramirez" ], ["chris"],
        ["sam"], ["mary"], ["kira"],["chase"],["porky"],
        ["pokey"],["shimmering black"],["mr byrd"], ["mr anderson"],
        ["coach clouse"], ["cheyanna"],["beasty"], ["brianna"],
         ['terious'], ["clayton"], ["mira"]


    ];
    thepuzzle = puzzlename[Math.floor(Math.random() * puzzlename.length)];
    word = thepuzzle[Math.floor(Math.random() * thepuzzle.length)];
    word = word.replace(/\s/g, "-");
    console.log(word);
    buttons();
    guesses = [ ];
    lives = 3;
    counter = 0;
    space = 0;
    result();
    comments();
    selectCat();
  }
  play();

 }
