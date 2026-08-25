"""Pocket TTS Voice Browser — listen to every catalog voice."""

from __future__ import annotations

import io
import threading
from contextlib import asynccontextmanager
from pathlib import Path

import numpy as np
import scipy.io.wavfile
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from voices import LANGUAGE_LABELS, VOICES, get_voice

STATIC_DIR = Path(__file__).parent / "static"

_model = None
_voice_cache: dict[str, object] = {}
_lock = threading.Lock()
_ready = False
_load_error: str | None = None


def _ensure_model():
    global _model, _ready, _load_error
    if _model is not None:
        return _model
    if _load_error:
        raise RuntimeError(_load_error)
    try:
        from pocket_tts import TTSModel

        print("Loading Pocket TTS model (first run may download weights)...")
        _model = TTSModel.load_model()
        _ready = True
        print("Model ready.")
        return _model
    except Exception as exc:  # noqa: BLE001
        _load_error = str(exc)
        raise


def _get_voice_state(voice_id: str):
    """Must be called while holding `_lock`."""
    if voice_id in _voice_cache:
        return _voice_cache[voice_id]
    model = _ensure_model()
    print(f"Loading voice: {voice_id}")
    state = model.get_state_for_audio_prompt(voice_id)
    _voice_cache[voice_id] = state
    return state


def _audio_to_wav_bytes(audio, sample_rate: int) -> bytes:
    arr = audio.detach().cpu().numpy() if hasattr(audio, "detach") else np.asarray(audio)
    arr = np.clip(arr.astype(np.float32), -1.0, 1.0)
    pcm = (arr * 32767.0).astype(np.int16)
    buf = io.BytesIO()
    scipy.io.wavfile.write(buf, sample_rate, pcm)
    return buf.getvalue()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Load model in a background thread so the UI is available immediately.
    def warmup():
        try:
            _ensure_model()
        except Exception as exc:  # noqa: BLE001
            print(f"Model load failed: {exc}")

    threading.Thread(target=warmup, daemon=True).start()
    yield


app = FastAPI(title="Pocket TTS Voice Browser", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class SpeakRequest(BaseModel):
    voice: str
    text: str | None = Field(default=None, max_length=500)


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/status")
def status():
    return {
        "ready": _ready,
        "error": _load_error,
        "voices_loaded": list(_voice_cache.keys()),
    }


@app.get("/api/voices")
def list_voices():
    return {
        "languages": LANGUAGE_LABELS,
        "voices": [
            {
                **v,
                "language_label": LANGUAGE_LABELS.get(v["language"], v["language"]),
            }
            for v in VOICES
        ],
    }


@app.post("/api/speak")
def speak(req: SpeakRequest):
    voice = get_voice(req.voice)
    if voice is None:
        raise HTTPException(status_code=404, detail=f"Unknown voice: {req.voice}")

    text = (req.text or "").strip() or voice["sample"]

    try:
        with _lock:
            model = _ensure_model()
            state = _get_voice_state(req.voice)
            audio = model.generate_audio(state, text)
            wav = _audio_to_wav_bytes(audio, model.sample_rate)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    return Response(
        content=wav,
        media_type="audio/wav",
        headers={"Content-Disposition": f'inline; filename="{req.voice}.wav"'},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=7860, reload=False)
