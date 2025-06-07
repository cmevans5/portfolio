# portfolio

This is a showcase of my coding projects through Codex.

## Demo Application

`app_demo.py` demonstrates a small reading assessment workflow. Run it from the
command line:

```bash
python app_demo.py
```

The script walks you through a short quiz to estimate reading level, generates a
story via OpenAI, then asks for an audio file to transcribe and align. It
requires an `OPENAI_API_KEY` environment variable for story generation and
online transcription. Whisper will be used locally if installed. After
alignment the script prints feedback for each word in the transcript.

Run tests and syntax checks with:

```bash
python -m unittest discover tests -v
python -m py_compile *.py
```
