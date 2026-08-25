const grid = document.getElementById("grid");
const textEl = document.getElementById("text");
const langFilter = document.getElementById("langFilter");
const statusDot = document.getElementById("statusDot");
const statusText = document.getElementById("statusText");

let voices = [];
let currentAudio = null;
let currentButton = null;

async function fetchStatus() {
  try {
    const res = await fetch("/api/status");
    const data = await res.json();
    if (data.error) {
      statusDot.className = "dot error";
      statusText.textContent = "Model failed to load";
      return;
    }
    if (data.ready) {
      statusDot.className = "dot ready";
      statusText.textContent = "Model ready";
    } else {
      statusDot.className = "dot";
      statusText.textContent = "Loading model…";
    }
  } catch {
    statusDot.className = "dot error";
    statusText.textContent = "Server offline";
  }
}

function render() {
  const lang = langFilter.value;
  const list = voices.filter((v) => lang === "all" || v.language === lang);
  grid.innerHTML = "";

  for (const voice of list) {
    const card = document.createElement("article");
    card.className = "voice";
    card.innerHTML = `
      <div class="voice-top">
        <div>
          <h2 class="voice-name">${voice.name}</h2>
          <div class="lang">${voice.language_label}</div>
        </div>
        <span class="badge">${voice.language}</span>
      </div>
      <button class="play" type="button" data-voice="${voice.id}">Play</button>
      <p class="meta" data-meta="${voice.id}"></p>
    `;
    grid.appendChild(card);
  }
}

async function playVoice(voiceId, button) {
  if (currentAudio) {
    currentAudio.pause();
    currentAudio = null;
  }
  if (currentButton && currentButton !== button) {
    currentButton.disabled = false;
    currentButton.classList.remove("playing");
    currentButton.textContent = "Play";
  }

  const meta = document.querySelector(`[data-meta="${voiceId}"]`);
  button.disabled = true;
  button.classList.add("playing");
  button.textContent = "Generating…";
  if (meta) {
    meta.className = "meta";
    meta.textContent = "Synthesizing…";
  }

  try {
    const res = await fetch("/api/speak", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        voice: voiceId,
        text: textEl.value.trim() || null,
      }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: res.statusText }));
      throw new Error(err.detail || "Generation failed");
    }

    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    const audio = new Audio(url);
    currentAudio = audio;
    currentButton = button;

    button.textContent = "Playing…";
    if (meta) meta.textContent = "Playing";

    audio.onended = () => {
      URL.revokeObjectURL(url);
      button.disabled = false;
      button.classList.remove("playing");
      button.textContent = "Play";
      if (meta) meta.textContent = "Done";
      currentAudio = null;
    };

    await audio.play();
  } catch (err) {
    button.disabled = false;
    button.classList.remove("playing");
    button.textContent = "Play";
    if (meta) {
      meta.className = "meta error";
      meta.textContent = err.message || "Failed";
    }
  }
}

grid.addEventListener("click", (event) => {
  const button = event.target.closest("button.play");
  if (!button) return;
  playVoice(button.dataset.voice, button);
});

langFilter.addEventListener("change", render);

async function boot() {
  const res = await fetch("/api/voices");
  const data = await res.json();
  voices = data.voices;

  for (const [code, label] of Object.entries(data.languages)) {
    const opt = document.createElement("option");
    opt.value = code;
    opt.textContent = label;
    langFilter.appendChild(opt);
  }

  render();
  await fetchStatus();
  setInterval(fetchStatus, 2500);
}

boot();
