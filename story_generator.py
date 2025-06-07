import os
from dataclasses import dataclass
from typing import List, Iterable

import openai

@dataclass
class StoryRequest:
    """Parameters for requesting a custom story."""

    reading_level: str
    topic: str
    target_words: List[str]
    sentences_per_page: int = 4
    pages: int = 1


def _create_story_prompt(req: StoryRequest) -> str:
    """Construct the prompt sent to the language model."""
    vocab = ", ".join(req.target_words) if req.target_words else ""
    page_instr = (
        f"Write {req.pages} page(s), each {req.sentences_per_page} sentences long. "
        "Insert '---' between pages. "
    )
    return (
        "You are an early reading assistant helping children learn to read. "
        f"Create a short story for level {req.reading_level} about {req.topic}. "
        f"Include these words: {vocab}. "
        f"{page_instr}Keep the tone friendly and engaging."
    )


def generate_story(req: StoryRequest) -> str:
    """Return a story generated from ``req`` using the OpenAI API."""
    prompt = _create_story_prompt(req)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.7,
    )
    story_text = response["choices"][0]["message"]["content"].strip()
    return story_text


def split_story_pages(story: str, marker: str = "---") -> List[str]:
    """Split a story into pages based on the page break marker."""
    return [page.strip() for page in story.split(marker) if page.strip()]


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate a short story for early readers.")
    parser.add_argument("--level", default="K", help="Reading level or grade (e.g., K, 1, 2)")
    parser.add_argument("--topic", required=True, help="Story topic, e.g., Dinosaurs")
    parser.add_argument(
        "--words", nargs="*", default=[], help="Target vocabulary words to include"
    )
    parser.add_argument(
        "--sentences",
        type=int,
        default=4,
        help="Sentences per page (3-6 recommended)",
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=1,
        help="Number of pages to generate",
    )
    args = parser.parse_args()

    req = StoryRequest(
        reading_level=args.level,
        topic=args.topic,
        target_words=args.words,
        sentences_per_page=args.sentences,
        pages=args.pages,
    )
    story = generate_story(req)
    print(story)


if __name__ == "__main__":
    # Requires OPENAI_API_KEY environment variable
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY environment variable not set")
    main()
