# AI Reading Companion for Kids

## Codex Workup: Instructions for Building the MVP

### Goal
Build a mobile app that generates personalized short stories for kids, listens as the child reads aloud, and gives real-time, supportive feedback based on their reading accuracy.

### Core Components Needed

1. **Story Generator (GPT Integration)**
   - Use GPT-4 (or similar) to generate short, age-appropriate stories.
   - Prompt should include: reading level, desired topic, target vocabulary words.
   - Output must be concise (3–6 sentences per page) and friendly in tone.
   - Optionally, add simple markup to indicate page breaks or illustration cues.

2. **Speech Recognition + Alignment**
   - Use a speech-to-text API (like Google Cloud Speech-to-Text or Whisper).
   - Align recognized text with the original story text in real time.
   - Identify:
     - Correctly pronounced words (green)
     - Mispronounced or skipped words (red)
     - Long pauses or hesitations (yellow, optional)
   - Codex should assist in formatting alignment logic (Levenshtein or diff-match-patch algorithms) and displaying interactive word-by-word progress.

3. **Feedback Mechanism**
   - Friendly mascot provides encouragement or correction suggestions.
   - After reading:
     - Display a summary of "words to practice."
     - Option to tap mispronounced word for definition/audio replay.
   - Codex can generate helper functions for word-to-speech playback (Text-to-Speech API) and tooltip popups with definitions or syllable breakdowns.

4. **UI Components**
   - Simple mobile interface using Flutter or React Native.
   - Pages should include:
     - Story reading view (text block with word-level feedback)
     - Theme prompt input (user chooses topics such as "Space" or "Dinosaurs")
     - Mascot panel for encouragement or corrections
     - Results view showing words missed and progress badges

5. **Data Logging**
   - Log reading sessions with:
     - Story ID
     - Accuracy percentage
     - Words flagged
   - Option to export summary for a parent or teacher
   - Codex can help create a simple localStorage or cloud-based database interface.

### MVP Tech Stack
- React Native for a cross-platform mobile app
- GPT API for story generation
- Google Speech-to-Text API or Whisper for real-time feedback
- Firebase or Supabase for user data and reading logs

### Future Features
- Adaptive difficulty progression
- Word games based on common mistakes
- Sibling/profiles support
- Offline mode with pre-cached stories and audio

### Monetization
- Freemium model: free tier includes three stories per week and basic feedback
- Premium option ($4.99/month) for unlimited stories, progress tracking, and more themes
- Affiliate links for real books (e.g., "Loved this space story? Buy 'AstroMouse!'")

### Coding Starter Tasks for Codex
1. Generate a story with a given topic, level, and five target words.
2. Build a function to highlight matched and mismatched words.
3. Scaffold the UI in React Native (storybook screen, mascot, and audio features).
4. Call the Google Speech API and stream feedback.
5. Store session accuracy and flagged words to Firebase.

### Next Step
Begin breaking down these modules into functions. Would you like to move on to story generation or audio alignment next?
