
function game() {
   let container = document.createElement('div');
   container.classList.add("heading");
   body.appendChild(container);
   let heading = document.createElement('h1');
   heading.textContent = "Rock Paper Scissors";
   container.appendChild(heading);

   let scoreBoard = document.createElement('div');
   scoreBoard.classList.add("scoreBoard");
   body.appendChild(scoreBoard);
   let title = document.createElement('h2');
   title.textContent = "Score";
   scoreBoard.appendChild(title);
   title.style.marginTop = "0px";
   title.style.marginBottom = "0px";

   let playerScore = document.createElement('div');
   scoreBoard.appendChild(playerScore);
   let pscore = document.createElement('p');
   pscore.textContent = "Player:";
   playerScore.appendChild(pscore);
   pscore.style.marginTop = "0px";
   pscore.style.marginBottom = "0px";

   let computerScore = document.createElement('div');
   scoreBoard.appendChild(computerScore);
   let cscore = document.createElement('p');
   cscore.textContent = "computer: ";
   computerScore.appendChild(cscore);
   cscore.style.marginTop = "0px";
   cscore.style.marginBottom = "0px";

   let choices = document.createElement('div');
   body.appendChild(choices);
   choices.classList.add('choices');

   let rock = document.createElement('p');
   choices.appendChild(rock);
   rock.textContent = "Rock \u2192 \u2191 \u2193 \u2192";
   rock.style.display = "flex";
   rock.style.justifyContent = 'center';
   rock.style.alignItems = 'center';
   rock.style.backgroundColor = "#1b1b1b";
   rock.style.color = "white";
   rock.style.width = "10%";

   let paper = document.createElement('p');
   choices.appendChild(paper);
   paper.style.display = "flex";
   paper.style.justifyContent = 'center';
   paper.style.alignItems = 'center';
   paper.textContent = "Paper";
   paper.style.backgroundColor = "white";
   paper.style.color = "black";
   paper.style.width = "10%";
   paper.style.height = "100px";
  

   let scissors = document.createElement('p');
   choices.appendChild(scissors);
   scissors.style.display = "flex";
   scissors.style.justifyContent = 'center';
   scissors.style.alignItems = 'center';
   scissors.textContent = "Scissors";
   scissors.style.backgroundColor = "grey";
   scissors.style.color = "white";
   scissors.style.width = "10%";
   scissors.style.height = "100px";
<<<<<<< HEAD
   scissors.style.border = "2px";

   let playerChoice;

   const Eagle500KG = ["w", "d", "s", "s", "s"];

   let stratagem = [];

   playerChoice = body.addEventListener('keydown', function (number) {
      let code = number.key;

      stratagem.push(code);

      if (stratagem === Eagle500KG) {
=======
   

   let playerChoice;
   
   const Eagle500KG = ["w", "d", "s", "s", "s" ];

   let stratagem = [];

   const allowedKeys = ['w', 'd', 's','a'];   

   
   playerChoice = body.addEventListener('keydown', function(event) {
      const code = event.key;

      stratagem.push(code);

      if (stratagem.toString() === Eagle500KG)
      {
>>>>>>> e23fe328d1cd823a6ed579b7bd03347fa70cd70c
         console.log('500kg dropped');
      }
       
      if(!allowedKeys.includes(code))
      {
         stratagem = [];
      }
      else if(stratagem.length > 5)
      {
            stratagem = [];
      };

      console.log(stratagem);
   });

<<<<<<< HEAD

=======
  
>>>>>>> e23fe328d1cd823a6ed579b7bd03347fa70cd70c

};

game();