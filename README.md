# Pocket TTS — Voice Browser

A local web app to listen to every built-in [Pocket TTS](https://github.com/kyutai-labs/pocket-tts) voice.

## Screenshots

### Home — pick a voice and play

![Voice Browser home](static/screenshots/voice-browser.png)

### Voice catalog

![Voice catalog grid](static/screenshots/voice-playing.png)

### Multilingual voices

![English and multilingual voices](static/screenshots/voice-catalog.png)

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
├── requirements.txt       # pip dependencies
├── pyproject.toml         # uv / project metadata
├── static/
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   └── screenshots/       # README images
└── README.md
```

## Notes

- First launch downloads model weights (needs internet). Later runs work offline.
- The first **Play** for each voice is slower (voice state loads once, then is cached).
- Keep the terminal open while using the browser.
