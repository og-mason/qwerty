let score = 0;

function sendGuess() {
  const input = document.getElementById("guess");
  const guess = parseInt(input.value);

  if (!guess || guess < 1 || guess > 100) {
    document.getElementById("result").innerText = "⚠️ Введи число от 1 до 100!";
    return;
  }

  const target = Math.floor(Math.random() * 100) + 1;
  const diff = Math.abs(guess - target);
  let result = "";

  if (diff === 0) {
    score += 3;
    result = `🎯 Точно! Загаданное число было ${target}. +3 очка`;
  } else if (diff <= 5) {
    score += 1;
    result = `👍 Почти! Загаданное число было ${target}. +1 очко`;
  } else {
    score -= 1;
    result = `❌ Не угадал. Загаданное число было ${target}. -1 очко`;
  }

  document.getElementById("result").innerText = result;
  document.getElementById("score").innerText = "Счёт: " + score;

  input.value = "";
}