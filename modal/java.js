let body = document.body;


function forKarl()
{
   console.log('The sound of democracy plays');
         let modal2 = document.createElement('div');
         modal2.classList.add('modal2');
         body.appendChild(modal2);

         let howTo = document.createElement('div');
         howTo.classList.add('howTo');
         modal2.appendChild(howTo);

         let button1 = document.createElement('button');
         button1.textContent = 'start';
         button1.classList.add('start');
         howTo.appendChild(button1);

         let text = document.createElement('h1');
         howTo.appendChild(text);
         text.textContent = "How to play";

         /*let helldiverpic = document.createElement('img'); //Get this image working!!!
         helldiverpic.width = 400;
         helldiverpic.height = 200; 
         helldiverpic.src = '/home/sobajer21/Desktop/helldiver/15bY.svg';
         howTo.appendChild(helldiverpic);*/

         /* Eventually add text to modal on how to play the game!*/

         function hide()
{
   modal2.style.display = "none";
   console.log('click');  
};
   button1.addEventListener("click", hide);
};

function modal(){


   let modal = document.createElement("div");
   modal.classList.add('modal');
   body.appendChild(modal);

   let content = document.createElement('div');
   modal.appendChild(content);
   content.classList.add('content');

   let video = document.createElement('video')
   content.appendChild(video);
   video.classList.add('video');
   video.src = "Helldiver.mp4";

   video.type = "video/mp4";
   video.controls = 'true';

   let exit = document.createElement('div');
   exit.classList.add('exit');
   modal.appendChild(exit);

   let x = document.createElement('span');
   x.classList.add('x');
   exit.appendChild(x);
   x.textContent = 'x';

   exit.addEventListener('click', function(){
      modal.style.display = "none";
      let audio = document.createElement('audio');
      body.appendChild(audio);
      let source = document.createElement('source');
      audio.appendChild(source);
      source.src = "hellDiversMain.mp3";
      source.type = "audio/mpeg"
      video.pause();

      audio.play().then(() => {
         forKarl();
      }).catch (error => {
         console.log("whoops")
      });
   });

   video.addEventListener("ended", function(){
      modal.style.display = "none";
      let audio = document.createElement('audio');
      body.appendChild(audio);
      let source = document.createElement('source');
      audio.appendChild(source);
      source.src = "hellDiversMain.mp3";
      source.type = "audio/mpeg";

      audio.play().then(() => {
         forKarl();
      }).catch (error => {
         console.log("whoops")
      });
   })

};

document.body.onload = modal();





