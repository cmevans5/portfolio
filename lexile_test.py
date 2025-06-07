"""Simple placeholder for a Lexile assessment.

This is a stub that in a real application would present passages of
different difficulty to the reader and analyze their performance to
estimate a Lexile range.
"""
from dataclasses import dataclass
from typing import List

@dataclass
class LexileQuestion:
    passage: str
    answer: str

@dataclass
class LexileResult:
    estimated_level: str
    score: int

SAMPLE_QUESTIONS: List[LexileQuestion] = [
    LexileQuestion(
        passage="The cat sat on the mat.",
        answer="cat"
    ),
    LexileQuestion(
        passage="The dog ran across the yard.",
        answer="dog"
    ),
]


def take_lexile_test(answers: List[str]) -> LexileResult:
    score = sum(1 for q, a in zip(SAMPLE_QUESTIONS, answers) if q.answer.lower() == a.lower())
    if score == len(SAMPLE_QUESTIONS):
        level = "1"
    else:
        level = "K"
    return LexileResult(estimated_level=level, score=score)


if __name__ == "__main__":
    # Example usage
    user_answers = [input(f"Read and answer: {q.passage} What is the key word? ") for q in SAMPLE_QUESTIONS]
    result = take_lexile_test(user_answers)
    print(f"Estimated reading level: {result.estimated_level} (score {result.score}/{len(SAMPLE_QUESTIONS)})")
