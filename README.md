# portfolio

This repository contains sample modules for a reading companion app.

## Story Generator

`story_generator.py` provides a simple interface to the OpenAI API to produce
short, age-appropriate stories. The `StoryRequest` dataclass captures the
desired reading level, topic, and target vocabulary words. You can also choose
how many sentences should appear on each page and how many pages to generate.
Page breaks are marked with `---` in the response. Make sure the
`OPENAI_API_KEY` environment variable is set before running.

```bash
python story_generator.py --level K --topic Dinosaurs \
  --words big loud roar --sentences 4 --pages 2
```

## Lexile Test (Prototype)

`lexile_test.py` is a small placeholder for assessing a student's reading level.
It presents short passages and checks answers to estimate a basic level.

```bash
python lexile_test.py
```

## Speech Recognition and Feedback (Prototype)

`reading_feedback.py` demonstrates how audio can be transcribed and
aligned with a passage to highlight correctly read words versus errors.
It requires the optional `whisper` package.

```bash
# Example: transcribe audio.wav and compare with a short sentence
python reading_feedback.py audio.wav "The cat sat on the mat."
```
