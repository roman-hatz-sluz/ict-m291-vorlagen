const dino = document.getElementById("game-dino");
const rock = document.getElementById("game-rock");
const score = document.getElementById("game-score");
const gameBox = document.getElementById("game");
const backgroundLayer1 = document.getElementById("bg-layer-1");
const backgroundLayer2 = document.getElementById("bg-layer-2");
const gameOver = document.getElementById("game-end");
const yourScore = document.getElementById("game-end-score");
const startScreen = document.getElementById("game-start");

let gameLoopInterval = 0;
const backgroundAudio = new Audio("./sounds/bg.mp3");
backgroundAudio.loop = true;
const jumpAudio = new Audio("./sounds/jump.mp3");
const crashAudio = new Audio("./sounds/crash.mp3");

const startGame = () => {
  gameOver.classList.add("hidden");
  backgroundLayer1.classList.add("bg-animation-layer-1");
  backgroundLayer2.classList.add("bg-animation-layer-2");
  rock.classList.add("rock-animation");
  dino.classList.add("dino-running");
  startScreen.classList.add("hidden");
  resetScore();
  backgroundAudio.play();
  startGameLoop();
};

const resetScore = () => {
  score.innerText = 0;
};

const jump = () => {
  jumpAudio.currentTime = 0;
  jumpAudio.play();
  dino.classList.add("jump-animation");
  setTimeout(() => {
    dino.classList.remove("jump-animation");
  }, 500);
};

const dieAnimation = () => {
  crashAudio.play();
  dino.classList.add("dino-dies");
  return new Promise((resolve) =>
    setTimeout(() => {
      dino.classList.remove("dino-dies");
      resolve();
    }, 500)
  );
};

gameBox.addEventListener("click", (event) => {
  if (!gameLoopInterval) {
    startGame();
  } else {
    if (!dino.classList.contains("jump-animation")) {
      jump();
    }
  }
});

const stopGame = async () => {
  gameLoopInterval = clearInterval(gameLoopInterval);
  backgroundLayer1.classList.remove("bg-animation-layer-1");
  backgroundLayer2.classList.remove("bg-animation-layer-2");
  rock.classList.remove("rock-animation");
  rock.classList.add("hidden");
  startScreen.classList.remove("hidden");
  dino.classList.remove("dino-running");
  gameOver.classList.remove("hidden");
  yourScore.innerText = Number(score.innerText) + 1;
  await dieAnimation();
  backgroundAudio.pause();
  backgroundAudio.currentTime = 0;
};

const startGameLoop = () => {
  gameLoopInterval = window.setInterval(() => {
    const dinoTop = parseInt(
      window.getComputedStyle(dino).getPropertyValue("top")
    );
    const rockLeft = parseInt(
      window.getComputedStyle(rock).getPropertyValue("left")
    );
    score.innerText = Number(score.innerText) + 1;
    if (rockLeft < 0) {
      rock.classList.add("hidden");
      const randomObstacleSpeed = Math.random() * 3 + 1; // random number between 1 and 3
      console.log(randomObstacleSpeed);
      rock.style.animation = `rock ${randomObstacleSpeed}s infinite linear`;
    } else {
      rock.classList.remove("hidden");
    }

    if (rockLeft < 50 && rockLeft > 0 && dinoTop > 150) {
      stopGame();
    }
  }, 50);
};
