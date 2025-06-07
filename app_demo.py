"""Demo application showing a simple reading assessment flow."""

from utils import take_lexile_test, generate_story, transcribe_audio, align_text


def main() -> None:
    level = take_lexile_test()
    story = generate_story(level)
    print("\nGenerated Story:\n", story, "\n")

    audio_file = input("Enter path to audio file for transcription: ").strip()
    transcript = transcribe_audio(audio_file)
    feedback = align_text(transcript, story)

    print("\nWord Feedback:")
    for item in feedback:
        print(f"{item['word']}: {item['status']}")


if __name__ == "__main__":
    main()
