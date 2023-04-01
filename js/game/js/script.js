
// function gameStart(){

//     document.getElementById('start').classList.add=('invisible')
//     document.querySelector('.obstacle').classList.add=('obstacleAni')


score = 0;
cross = true;
endGame=false;

audio = new Audio('/assets/music.mp3');
audiogo = new Audio('/assets/gameover.mp3');

var timer = setTimeout(() => {
    audio.play()
}, 1000);

 
// ---------------------------------player move----------------------------------------------------

document.onkeydown = function (e) {
    // console.log("Key code is: ", e.keyCode)
    if (e.keyCode == 38) {
        dino = document.querySelector('.dino');
        dino.classList.add('animateDino');
        setTimeout(() => {
            dino.classList.remove('animateDino')
        }, 500);
    }
    if (e.keyCode == 39) {
        dino = document.querySelector('.dino');
        dinoX = parseInt(window.getComputedStyle(dino, null).getPropertyValue('left'));
           if(1170 > dinoX)
           dino.style.left = dinoX + 112 + "px";

             
         
    }
    if (e.keyCode == 37) {
        dino = document.querySelector('.dino');
        dinoX = parseInt(window.getComputedStyle(dino, null).getPropertyValue('left'));
 
        if(52<dinoX)
        dino.style.left = (dinoX - 112) + "px";
    }
}

// ---------------------------------Annimation and Score----------------------------------------------------

timer=setInterval(() => {
    dino = document.querySelector('.dino');
    gameOver = document.querySelector('.gameOver');
    obstacle = document.querySelector('.obstacle');

    dx = parseInt(window.getComputedStyle(dino, null).getPropertyValue('left'));
    dy = parseInt(window.getComputedStyle(dino, null).getPropertyValue('top'));

    ox = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('left'));
    oy = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('top'));

    offsetX = Math.abs(dx - ox);
    offsetY = Math.abs(dy - oy);
    
    if (offsetX < 73 && offsetY < 52) {
         gameOver.innerHTML = "Game Over - Reload to Play Again"
        endGame=true;
          obstacle.classList.remove('obstacleAni')
        // dino.classList.remove('animateDino')
        audiogo.play();
        setTimeout(() => {
            audiogo.pause();
            audio.pause();
        }, 1000);

        for(let i =0;i<input.length;i++){
            
            setTimeout(show(i),1000)
        }
    }
    else if (offsetX < 145 && cross) {
        score += 1;
        show(score - 1)
        if(score<7){
        scoreCont.innerHTML = "Your Score: " + score
        }
        cross = false;
        setTimeout(() => {
            cross = true;
        }, 1000);

        setTimeout(() => {
            aniDur = parseFloat(window.getComputedStyle(obstacle, null).getPropertyValue('animation-duration'));
            newDur = aniDur - 0.1;
            obstacle.style.animationDuration = newDur + 's';
            console.log('New animation duration: ', newDur)
        }, 700);

    }
    if(score==6){
       gameOver.innerHTML="You Win Now Please Fill the Form"
        obstacle.classList.remove('obstacleAni')
        endGame=true;
        // dino.classList.remove('animateDino')
    }

}, 10);
 

// ---------------------------------Dynamic Form with DB entry----------------------------------------------------


const input =[{entry:'firstname' , type:'text'},{entry:'lastname' , type:'text'},{entry:'email' , type:'email'},{entry:'designation' , type:'text'},{entry:'mobile' , type:'number'},{entry:'organization',text:'text'}]
  
str = ""
existArr = []
p = 0


function show(id) {
   
   
    if (!existArr.includes(id)&& id<6) {

            st=$(`
            <div class="col-md-4">
              <div class="form-floating mb-2 ">
              <input class="form-control" id="${input[id].entry}" type=${input[id].type} name=${input[id].entry} placeholder="abcd"></input> 
              <label for="${input[id].entry}" >${input[id].entry} </label>
              </div>
            </div>
             `)
             
        
        $('#contact-form').append(st)
        existArr.push(id)

        win=document.getElementById('trophy')
        win.innerHTML =` ${existArr.length}/6`
       
    }
    
}

// ---------------------------------Timer Function----------------------------------------------------


var timeLeft = 30; 
var timerId = setInterval(countdown, 1000);

function countdown() {
  if (timeLeft == -1 || endGame) {
      document.getElementById('submit').classList.remove('invisible')
      document.getElementById('timerid').classList.add('invisible')
      clearTimeout(timerId);
     
  } 
 
  else {
   
   document.getElementById('timerid').innerHTML = timeLeft + ' seconds remaining';

   p += 3.333
   progress = document.getElementById('progressid').style.width = `${p}%`
     
    timeLeft--;
  }
}


// ---------------------------------Form Submition----------------------------------------------------

function formSubmit(){
   
    const formdata=new FormData()

    for(let i=0;i<input.length;i++){
        formdata.append(input[i].entry, document.getElementsByName(input[i].entry)[0].value)
    }

console.log("Form Data => ",formdata)

}







// }

