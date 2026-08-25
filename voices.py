"""Catalog of Pocket TTS built-in voices."""

from __future__ import annotations

VOICES: list[dict[str, str]] = [
    # Default language voices (English model works for all catalog names)
    {"id": "alba", "name": "Alba", "language": "en", "sample": "Hello, my name is Alba."},
    {"id": "anna", "name": "Anna", "language": "en", "sample": "Hello, my name is Anna."},
    {"id": "azelma", "name": "Azelma", "language": "en", "sample": "Hello, my name is Azelma."},
    {"id": "bill_boerst", "name": "Bill Boerst", "language": "en", "sample": "Hello, my name is Bill Boerst."},
    {"id": "caro_davy", "name": "Caro Davy", "language": "en", "sample": "Hello, my name is Caro Davy."},
    {"id": "charles", "name": "Charles", "language": "en", "sample": "Hello, my name is Charles."},
    {"id": "cosette", "name": "Cosette", "language": "en", "sample": "Hello, my name is Cosette."},
    {"id": "eponine", "name": "Eponine", "language": "en", "sample": "Hello, my name is Eponine."},
    {"id": "eve", "name": "Eve", "language": "en", "sample": "Hello, my name is Eve."},
    {"id": "fantine", "name": "Fantine", "language": "en", "sample": "Hello, my name is Fantine."},
    {"id": "george", "name": "George", "language": "en", "sample": "Hello, my name is George."},
    {"id": "jane", "name": "Jane", "language": "en", "sample": "Hello, my name is Jane."},
    {"id": "jean", "name": "Jean", "language": "en", "sample": "Hello, my name is Jean."},
    {"id": "javert", "name": "Javert", "language": "en", "sample": "Hello, my name is Javert."},
    {"id": "marius", "name": "Marius", "language": "en", "sample": "Hello, my name is Marius."},
    {"id": "mary", "name": "Mary", "language": "en", "sample": "Hello, my name is Mary."},
    {"id": "michael", "name": "Michael", "language": "en", "sample": "Hello, my name is Michael."},
    {"id": "paul", "name": "Paul", "language": "en", "sample": "Hello, my name is Paul."},
    {"id": "peter_yearsley", "name": "Peter Yearsley", "language": "en", "sample": "Hello, my name is Peter Yearsley."},
    {"id": "stuart_bell", "name": "Stuart Bell", "language": "en", "sample": "Hello, my name is Stuart Bell."},
    {"id": "vera", "name": "Vera", "language": "en", "sample": "Hello, my name is Vera."},
    # Non-English catalog voices
    {"id": "estelle", "name": "Estelle", "language": "fr", "sample": "Bonjour, je m'appelle Estelle."},
    {"id": "giovanni", "name": "Giovanni", "language": "it", "sample": "Ciao, mi chiamo Giovanni."},
    {"id": "lola", "name": "Lola", "language": "es", "sample": "Hola, me llamo Lola."},
    {"id": "juergen", "name": "Juergen", "language": "de", "sample": "Hallo, ich heiße Juergen."},
    {"id": "rafael", "name": "Rafael", "language": "pt", "sample": "Olá, o meu nome é Rafael."},
]

LANGUAGE_LABELS = {
    "en": "English",
    "fr": "French",
    "it": "Italian",
    "es": "Spanish",
    "de": "German",
    "pt": "Portuguese",
}


def get_voice(voice_id: str) -> dict[str, str] | None:
    for voice in VOICES:
        if voice["id"] == voice_id:
            return voice
    return None
