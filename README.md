# Pocket TTS — Voice Browser

A local web app to listen to every built-in [Pocket TTS](https://github.com/kyutai-labs/pocket-tts) voice.

## Screenshots

### Home — pick a voice and play

![Voice Browser home](static/screenshots/voice-browser.png)

### Voice catalog

![Voice catalog grid](static/screenshots/voice-playing.png)

### Multilingual voices

![English and multilingual voices](static/screenshots/voice-catalog.png)

## Listen to every voice

GitHub README pages **cannot embed audio players** (HTML `<audio>` is stripped). Use one of these instead:

1. **Best:** open the [Listen gallery](listen.html) after enabling GitHub Pages (see below), or open any sample file below — GitHub’s file page has a built-in player.
2. **Quick:** click **▶ Listen** on a voice (opens the `.wav` with GitHub’s player).

### English

| Voice | Sample | Listen |
| --- | --- | --- |
| Alba | Hello, my name is Alba. | [▶ Listen](samples/alba.wav) |
| Anna | Hello, my name is Anna. | [▶ Listen](samples/anna.wav) |
| Azelma | Hello, my name is Azelma. | [▶ Listen](samples/azelma.wav) |
| Bill Boerst | Hello, my name is Bill Boerst. | [▶ Listen](samples/bill_boerst.wav) |
| Caro Davy | Hello, my name is Caro Davy. | [▶ Listen](samples/caro_davy.wav) |
| Charles | Hello, my name is Charles. | [▶ Listen](samples/charles.wav) |
| Cosette | Hello, my name is Cosette. | [▶ Listen](samples/cosette.wav) |
| Eponine | Hello, my name is Eponine. | [▶ Listen](samples/eponine.wav) |
| Eve | Hello, my name is Eve. | [▶ Listen](samples/eve.wav) |
| Fantine | Hello, my name is Fantine. | [▶ Listen](samples/fantine.wav) |
| George | Hello, my name is George. | [▶ Listen](samples/george.wav) |
| Jane | Hello, my name is Jane. | [▶ Listen](samples/jane.wav) |
| Jean | Hello, my name is Jean. | [▶ Listen](samples/jean.wav) |
| Javert | Hello, my name is Javert. | [▶ Listen](samples/javert.wav) |
| Marius | Hello, my name is Marius. | [▶ Listen](samples/marius.wav) |
| Mary | Hello, my name is Mary. | [▶ Listen](samples/mary.wav) |
| Michael | Hello, my name is Michael. | [▶ Listen](samples/michael.wav) |
| Paul | Hello, my name is Paul. | [▶ Listen](samples/paul.wav) |
| Peter Yearsley | Hello, my name is Peter Yearsley. | [▶ Listen](samples/peter_yearsley.wav) |
| Stuart Bell | Hello, my name is Stuart Bell. | [▶ Listen](samples/stuart_bell.wav) |
| Vera | Hello, my name is Vera. | [▶ Listen](samples/vera.wav) |

### Other languages

| Voice | Language | Sample | Listen |
| --- | --- | --- | --- |
| Estelle | French | Bonjour, je m'appelle Estelle. | [▶ Listen](samples/estelle.wav) |
| Giovanni | Italian | Ciao, mi chiamo Giovanni. | [▶ Listen](samples/giovanni.wav) |
| Lola | Spanish | Hola, me llamo Lola. | [▶ Listen](samples/lola.wav) |
| Juergen | German | Hallo, ich heiße Juergen. | [▶ Listen](samples/juergen.wav) |
| Rafael | Portuguese | Olá, o meu nome é Rafael. | [▶ Listen](samples/rafael.wav) |

All files: [`samples/`](samples/) · Gallery page: [`listen.html`](listen.html)

### Enable the Listen gallery (GitHub Pages)

1. Repo **Settings** → **Pages**
2. **Source:** Deploy from a branch
3. Branch: `main` / folder: `/ (root)` → Save
4. Open: `https://hamzaraouf.github.io/pocket-tts-setup/listen.html`

## Requirements

- Python **3.11+**
- Internet on first run (downloads Pocket TTS model weights)
- Works on **CPU** (no GPU required)

## Setup

### Option A — with `pip` + `requirements.txt`

```bash
# 1. Go to the project folder
cd Pocket-tts

# 2. Create a virtual environment
python3 -m venv .venv

# 3. Activate it
# macOS / Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt
```

### Option B — with `uv` (recommended)

```bash
cd Pocket-tts
uv sync
```

## Run

### With pip / venv

```bash
source .venv/bin/activate   # skip if already activated
python app.py
```

### With uv

```bash
uv run python app.py
```

Then open **http://127.0.0.1:7860** in your browser.

Stop the server with `Ctrl+C`.

## What you can do

- Browse all 26 catalog voices (EN / FR / IT / ES / DE / PT)
- Filter by language
- Play each voice’s default sample
- Type custom text and hear it in any voice

## Project structure

```text
Pocket-tts/
├── app.py                 # FastAPI server
├── voices.py              # Voice catalog
├── listen.html            # Standalone listen gallery (GitHub Pages)
├── requirements.txt       # pip dependencies
├── pyproject.toml         # uv / project metadata
├── samples/               # 16-bit PCM WAV per voice
├── scripts/
│   └── generate_samples.py
├── static/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── screenshots/
└── README.md
```

## Regenerate voice samples

```bash
uv run python scripts/generate_samples.py
```

## Notes

- First launch downloads model weights (needs internet). Later runs work offline.
- The first **Play** for each voice is slower (voice state loads once, then is cached).
- Keep the terminal open while using the browser.
- Sample WAVs are **16-bit PCM** so GitHub’s built-in player can play them.
