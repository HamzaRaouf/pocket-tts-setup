"""Generate one sample WAV per catalog voice for the README."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import scipy.io.wavfile
from pocket_tts import TTSModel

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from voices import LANGUAGE_LABELS, VOICES  # noqa: E402

OUT_DIR = ROOT / "samples"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Loading Pocket TTS model...")
    model = TTSModel.load_model()
    print("Model ready. Generating samples...")

    for i, voice in enumerate(VOICES, start=1):
        voice_id = voice["id"]
        out_path = OUT_DIR / f"{voice_id}.wav"
        print(f"[{i}/{len(VOICES)}] {voice['name']} ({LANGUAGE_LABELS[voice['language']]}) -> {out_path.name}")
        state = model.get_state_for_audio_prompt(voice_id)
        audio = model.generate_audio(state, voice["sample"])
        arr = audio.detach().cpu().numpy().astype(np.float32)
        arr = np.clip(arr, -1.0, 1.0)
        # GitHub / browsers play 16-bit PCM WAV; float WAV often fails.
        pcm = (arr * 32767.0).astype(np.int16)
        scipy.io.wavfile.write(out_path, model.sample_rate, pcm)

    print(f"Done. Wrote {len(VOICES)} files to {OUT_DIR}")


if __name__ == "__main__":
    main()
