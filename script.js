function corruptReality() {
    const text = document.getElementById("text");
    text.innerText = getRandomInsanity();
  
    for (let i = 0; i < 5; i++) {
      let popup = document.createElement('div');
      popup.innerText = getRandomInsanity();
      popup.style.position = 'fixed';
      popup.style.top = Math.random() * 100 + 'vh';
      popup.style.left = Math.random() * 100 + 'vw';
      popup.style.color = getRandomColor();
      popup.style.fontSize = Math.random() * 5 + 1 + 'em';
      popup.style.transform = `rotate(${Math.random() * 360}deg)`;
      popup.style.zIndex = 999;
      popup.style.pointerEvents = 'none';
      document.body.appendChild(popup);
      setTimeout(() => popup.remove(), 3000);
    }
  
    if (Math.random() > 0.9) {
      const audio = new Audio('https://upload.wikimedia.org/wikipedia/commons/4/45/Scream.ogg');
      audio.play();
    }
  
    document.body.style.transform = `scale(${1 + Math.random() * 0.01}) rotate(${Math.random()}rad)`;
  }
  
  function getRandomInsanity() {
    const phrases = [
      "█████ has left the simulation",
      "𓆩NULL𓆪",
      "404: GOD NOT FOUND",
      "subsystem overflow",
      "» ты проснулся?",
      "🧠 undefined ⤵",
      "disconnecting reality...",
      "dream_core.exe"
    ];
    return phrases[Math.floor(Math.random() * phrases.length)];
  }
  
  function getRandomColor() {
    return `hsl(${Math.floor(Math.random() * 360)}, 100%, 70%)`;
  }
  