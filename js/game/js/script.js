score = 0;
cross = true;

audio = new Audio('/assets/music.mp3');
audiogo = new Audio('/assets/gameover.mp3');

var timer = setTimeout(() => {
    audio.play()
}, 1000);

document.onkeydown = function (e) {
    console.log("Key code is: ", e.keyCode)
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
        dino.style.left = dinoX + 112 + "px";
    }
    if (e.keyCode == 37) {
        dino = document.querySelector('.dino');
        dinoX = parseInt(window.getComputedStyle(dino, null).getPropertyValue('left'));
        dino.style.left = (dinoX - 112) + "px";
    }
}

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
    // console.log(offsetX, offsetY)
    if (offsetX < 73 && offsetY < 52) {
        gameOver.innerHTML = "Game Over - Reload to Play Again"
        obstacle.classList.remove('obstacleAni')
        audiogo.play();
        setTimeout(() => {
            audiogo.pause();
            audio.pause();
        }, 1000);
    }
    else if (offsetX < 145 && cross) {
        score += 1;
        show(score - 1)
        updateScore(score);
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
    }

}, 10);

function updateScore(score) {
    scoreCont.innerHTML = "Your Score: " + score
}

const input =[{firstName:'name' , type:'text',placeholder:"name"},{lastName:'last' , type:'text'},{email:'email' , type:'email'}]
// inputs = ['FirstName', 'LastName', 'Email', 'Designation', 'Mobile', 'Organization']
str = ""
existArr = []
p = 0

function show(id) {
    if (!existArr.includes(id)&& id<6) {
        // tag = document.getElementById('contact-form')
        str = $('<input type="'+input[0].type+'" name="'+input[0].firstName+'" placeholder="'+input[0].placeholder+'">')
        form = $('<form class="game"></form>')
        input = $('<input type="'+input[0].type+'" name="'+input[0].firstName+'" placeholder="'+input[0].placeholder+'">')
        input1 = $('<input type="'+input[0].type+'" name="'+input[0].firstName+'" placeholder="'+input[0].placeholder+'">')
        form.append(input)
        form.append(input1)
        // str += `
        // <div class="col-md-4">
        //  <div class="row">
        //   <div class="form-floating mb-2 col-md-6">
        //    <input class="form-control" type="text" name="${inputs[id]}"> </input>
        //    <label for="${inputs[id]}" class="form-label">${inputs[id]}</label>
        //   </div>
        //  </div>
        // </div>` 

        // tag.innerHTML = str
        $('#contact-form').append(form)
        existArr.push(id)

        p += 16.667
        progress = document.getElementById('progressid').style.width = `${p}%`
         
         win=document.getElementById('trophy')
         win.innerHTML =` ${existArr.length}/6`
    }
    else {
        console.log("Already Exist...")
    }
}