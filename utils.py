"""Utility functions for the demo application."""

from typing import List, Dict
import os

import openai

try:
    import whisper  # type: ignore
except Exception:  # whisper is optional
    whisper = None


def take_lexile_test() -> int:
    """Run a simple interactive Lexile-like quiz and return an estimated level."""
    questions = [
        ("Which word is opposite of 'big'?", {"a": "tiny", "b": "huge", "c": "large"}, "a"),
        ("Choose the noun:", {"a": "run", "b": "cat", "c": "quickly"}, "b"),
        ("Which is a verb?", {"a": "jump", "b": "blue", "c": "tree"}, "a"),
    ]
    score = 0
    for prompt, options, answer in questions:
        print(prompt)
        for key, val in options.items():
            print(f" {key}) {val}")
        response = input("Your answer: ").strip().lower()
        if response == answer:
            score += 1
    level = 200 + score * 100
    print(f"Estimated reading level: {level}")
    return level


def generate_story(level: int) -> str:
    """Generate a short story for a given reading level using OpenAI."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = (
        "Write a short, age-appropriate story for a child with reading level "
        f"{level}."
    )
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful story generator."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=120,
        )
        return resp["choices"][0]["message"]["content"].strip()
    except Exception as exc:  # fallback to deterministic story on failure
        print("Story generation failed:", exc)
        return (
            f"Once upon a time, at reading level {level}, "
            "there lived a coder who loved to write programs."
        )


def transcribe_audio(filename: str) -> str:
    """Transcribe audio from a file using Whisper or OpenAI."""
    print(f"Transcribing {filename} ...")
    if whisper is not None:
        try:
            model = whisper.load_model("base")
            result = model.transcribe(filename)
            return result["text"].strip()
        except Exception as exc:
            print("Local Whisper failed:", exc)
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        with open(filename, "rb") as f:
            resp = openai.Audio.transcribe("whisper-1", f)
        return resp["text"].strip()
    except Exception as exc:
        print("OpenAI transcription failed:", exc)
        return "transcription unavailable"


def align_text(transcript: str, reference: str) -> List[Dict[str, str]]:
    """Align a transcript with reference text and provide word feedback."""
    transcript_words = transcript.split()
    ref_words = reference.split()
    feedback = []
    for idx, word in enumerate(transcript_words):
        status = "ok"
        if idx >= len(ref_words) or word.lower() != ref_words[idx].lower():
            status = "diff"
        feedback.append({"word": word, "status": status})
    return feedback
