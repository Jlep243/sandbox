
function game()
{
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
   rock.style.width = "200px";
   rock.style.height = "100px";
   rock.style.border = '2px';

   let paper = document.createElement('p');
   choices.appendChild(paper);
   paper.style.display = "flex";
   paper.style.justifyContent = 'center';
   paper.style.alignItems = 'center';
   paper.textContent = "Paper";
   paper.style.backgroundColor = "white";
   paper.style.color = "black";
   paper.style.width = "200px";
   paper.style.height = "100px";
   paper.style.border = '2px';

   let scissors = document.createElement('p');
   choices.appendChild(scissors);
   scissors.style.display = "flex";
   scissors.style.justifyContent = 'center';
   scissors.style.alignItems = 'center';
   scissors.textContent = "Scissors";
   scissors.style.backgroundColor = "grey";
   scissors.style.color = "white";
   scissors.style.width = "200px";
   scissors.style.height = "100px";
   scissors.style.border = "2px"; 

   let playerChoice;
   

   playerChoice = body.addEventListener('keydown', function(number){
      let code = number.key;
      
 
   
      const Eagle500KG = ["w", "d", "s", "s", "s" ];
      //make a loop in where every time it loops it adds a variable to the array
      // This way it makes the array final and then pushes another variable to the end
      //let code = number.key;


      let stratagem = [];
      stratagem.push(code);

      console.log(stratagem);
      if (stratagem.toString() == Eagle500KG)
      {
         console.log('500kg dropped');
      };
   });
   
  

};

game();