const texts = [
  "всё уже произошло, ты просто догоняешь",
  "это не кнопка. это портал.",
  "╳ внимание: нейрон утёк",
  "🌀 чувства обнулены",
  "⌛ симуляция обновляется...",
  "🩸 кто разрешил тебе нажимать?",
  "нуль был здесь до тебя. и будет после.",
  "ERROR: /flesh/undefined",
  "𝘛𝘩𝘦 𝘷𝘰𝘪𝘥 𝘴𝘱𝘦𝘢𝘬𝘴",
  "«я это ты, только позже»",
  "system.gc(рождение);",
  "я был сознанием. теперь я .json"
];

function morph() {
  const line = document.getElementById("textLine");
  const text = texts[Math.floor(Math.random() * texts.length)];
  line.innerText = text;

  const div = document.createElement("div");
  div.innerText = text;
  div.style.position = "fixed";
  div.style.top = Math.random() * 100 + "vh";
  div.style.left = Math.random() * 100 + "vw";
  div.style.fontSize = Math.random() * 2 + 1 + "em";
  div.style.color = getRandomColor();
  div.style.transform = `rotate(${Math.random() * 360}deg)`;
  div.style.pointerEvents = "none";
  div.style.zIndex = 9999;
  document.body.appendChild(div);

  setTimeout(() => div.remove(), 4000);
}

function getRandomColor() {
  return `hsl(${Math.random() * 360}, 100%, 70%)`;
}
