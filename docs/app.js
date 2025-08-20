// app.js
let score = 0;

window.onload = function() {
  document.getElementById("checkBtn").addEventListener("click", sendGuess);
};

function sendGuess() {
  const input = document.getElementById("guess");
  const guess = parseInt(input.value);

  if (!guess || guess < 1 || guess > 100) {
    showResult("⚠️ Введи число от 1 до 100!");
    return;
  }

  const target = Math.floor(Math.random() * 100) + 1;
  const diff = Math.abs(guess - target);
  let result = "";
  let points = 0;

  if (diff === 0) {
    points = 3;
    result = `🎯 Точно! Загаданное число было ${target}. +3 очка`;
  } else if (diff <= 5) {
    points = 1;
    result = `👍 Почти! Загаданное число было ${target}. +1 очко`;
  } else {
    points = -1;
    result = `❌ Не угадал. Загаданное число было ${target}. -1 очко`;
  }

  score += points;
  showResult(result);
  updateScore(score);

  if (points > 0) {
    for (let i = 0; i < points; i++) createStar();
  }

  input.value = "";
}

function showResult(text) {
  const resultEl = document.getElementById("result");
  resultEl.innerText = text;
}

function updateScore(value) {
  document.getElementById("score").innerText = "Счёт: " + value;
}

function createStar() {
  const star = document.createElement("span");
  star.className = "star";
  star.innerText = "⭐";
  const container = document.querySelector(".container");
  star.style.left = `${50 + Math.random() * 100}px`;
  star.style.top = "0px";
  container.appendChild(star);

  setTimeout(() => star.remove(), 1000);
}
