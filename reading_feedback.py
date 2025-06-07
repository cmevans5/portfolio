"""Speech recognition and word-level alignment prototype.

This module provides utilities to transcribe audio using Whisper and
compare the recognized text against a target passage. The goal is to
highlight words that were read correctly, mispronounced, or skipped.
"""
from dataclasses import dataclass
from typing import List, Tuple
import difflib

try:
    import whisper  # type: ignore
except ImportError:  # pragma: no cover - optional dependency
    whisper = None


@dataclass
class WordFeedback:
    word: str
    status: str  # 'correct', 'mispronounced', or 'skipped'


def transcribe_audio(path: str) -> str:
    """Transcribe ``path`` with Whisper if available.

    Parameters
    ----------
    path:
        Path to an audio file.

    Returns
    -------
    str
        Recognized text. If Whisper is not installed, an empty string is
        returned.
    """
    if whisper is None:
        raise RuntimeError("whisper package not installed")

    model = whisper.load_model("base")
    result = model.transcribe(path)
    return result.get("text", "").strip()


def align_text(expected: str, actual: str) -> List[WordFeedback]:
    """Compare expected and actual text word by word.

    The function performs a diff between the expected passage and the
    recognized text. It returns a list of ``WordFeedback`` indicating
    whether each expected word was read correctly, replaced, or skipped.
    """
    expected_words = expected.split()
    actual_words = actual.split()

    matcher = difflib.SequenceMatcher(a=expected_words, b=actual_words)
    feedback: List[WordFeedback] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            for w in expected_words[i1:i2]:
                feedback.append(WordFeedback(word=w, status="correct"))
        elif tag == "replace":
            for w in expected_words[i1:i2]:
                feedback.append(WordFeedback(word=w, status="mispronounced"))
        elif tag == "delete":
            for w in expected_words[i1:i2]:
                feedback.append(WordFeedback(word=w, status="skipped"))
        elif tag == "insert":
            # words inserted by the reader are ignored in this prototype
            continue
    return feedback


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Transcribe audio and align with a text passage.")
    parser.add_argument("audio_file", help="Path to the recorded reading")
    parser.add_argument("passage", help="Text the user was expected to read")
    args = parser.parse_args()

    recognized = transcribe_audio(args.audio_file)
    print("Recognized:\n", recognized)

    fb = align_text(args.passage, recognized)
    print("\nFeedback:")
    for item in fb:
        print(f"{item.word}: {item.status}")

