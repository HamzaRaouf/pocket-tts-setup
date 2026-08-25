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

Click **Play** in the player, or open the file link if the player does not appear.

### English

| Voice | Sample | Listen |
| --- | --- | --- |
| Alba | Hello, my name is Alba. | <audio controls preload="none" src="samples/alba.wav"></audio> [alba.wav](samples/alba.wav) |
| Anna | Hello, my name is Anna. | <audio controls preload="none" src="samples/anna.wav"></audio> [anna.wav](samples/anna.wav) |
| Azelma | Hello, my name is Azelma. | <audio controls preload="none" src="samples/azelma.wav"></audio> [azelma.wav](samples/azelma.wav) |
| Bill Boerst | Hello, my name is Bill Boerst. | <audio controls preload="none" src="samples/bill_boerst.wav"></audio> [bill_boerst.wav](samples/bill_boerst.wav) |
| Caro Davy | Hello, my name is Caro Davy. | <audio controls preload="none" src="samples/caro_davy.wav"></audio> [caro_davy.wav](samples/caro_davy.wav) |
| Charles | Hello, my name is Charles. | <audio controls preload="none" src="samples/charles.wav"></audio> [charles.wav](samples/charles.wav) |
| Cosette | Hello, my name is Cosette. | <audio controls preload="none" src="samples/cosette.wav"></audio> [cosette.wav](samples/cosette.wav) |
| Eponine | Hello, my name is Eponine. | <audio controls preload="none" src="samples/eponine.wav"></audio> [eponine.wav](samples/eponine.wav) |
| Eve | Hello, my name is Eve. | <audio controls preload="none" src="samples/eve.wav"></audio> [eve.wav](samples/eve.wav) |
| Fantine | Hello, my name is Fantine. | <audio controls preload="none" src="samples/fantine.wav"></audio> [fantine.wav](samples/fantine.wav) |
| George | Hello, my name is George. | <audio controls preload="none" src="samples/george.wav"></audio> [george.wav](samples/george.wav) |
| Jane | Hello, my name is Jane. | <audio controls preload="none" src="samples/jane.wav"></audio> [jane.wav](samples/jane.wav) |
| Jean | Hello, my name is Jean. | <audio controls preload="none" src="samples/jean.wav"></audio> [jean.wav](samples/jean.wav) |
| Javert | Hello, my name is Javert. | <audio controls preload="none" src="samples/javert.wav"></audio> [javert.wav](samples/javert.wav) |
| Marius | Hello, my name is Marius. | <audio controls preload="none" src="samples/marius.wav"></audio> [marius.wav](samples/marius.wav) |
| Mary | Hello, my name is Mary. | <audio controls preload="none" src="samples/mary.wav"></audio> [mary.wav](samples/mary.wav) |
| Michael | Hello, my name is Michael. | <audio controls preload="none" src="samples/michael.wav"></audio> [michael.wav](samples/michael.wav) |
| Paul | Hello, my name is Paul. | <audio controls preload="none" src="samples/paul.wav"></audio> [paul.wav](samples/paul.wav) |
| Peter Yearsley | Hello, my name is Peter Yearsley. | <audio controls preload="none" src="samples/peter_yearsley.wav"></audio> [peter_yearsley.wav](samples/peter_yearsley.wav) |
| Stuart Bell | Hello, my name is Stuart Bell. | <audio controls preload="none" src="samples/stuart_bell.wav"></audio> [stuart_bell.wav](samples/stuart_bell.wav) |
| Vera | Hello, my name is Vera. | <audio controls preload="none" src="samples/vera.wav"></audio> [vera.wav](samples/vera.wav) |

### Other languages

| Voice | Language | Sample | Listen |
| --- | --- | --- | --- |
| Estelle | French | Bonjour, je m'appelle Estelle. | <audio controls preload="none" src="samples/estelle.wav"></audio> [estelle.wav](samples/estelle.wav) |
| Giovanni | Italian | Ciao, mi chiamo Giovanni. | <audio controls preload="none" src="samples/giovanni.wav"></audio> [giovanni.wav](samples/giovanni.wav) |
| Lola | Spanish | Hola, me llamo Lola. | <audio controls preload="none" src="samples/lola.wav"></audio> [lola.wav](samples/lola.wav) |
| Juergen | German | Hallo, ich heiße Juergen. | <audio controls preload="none" src="samples/juergen.wav"></audio> [juergen.wav](samples/juergen.wav) |
| Rafael | Portuguese | Olá, o meu nome é Rafael. | <audio controls preload="none" src="samples/rafael.wav"></audio> [rafael.wav](samples/rafael.wav) |

All sample files live in [`samples/`](samples/).

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
├── samples/               # Pre-generated WAV for each voice (README)
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
