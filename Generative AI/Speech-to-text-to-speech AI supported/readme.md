# Voice Assistant Project

## Introduction

The project aims to create a voice assistant powered by OpenAI's GPT-3.5 Turbo model, enhancing the capabilities beyond existing systems like Alexa. The assistant waits for a wake word ("hey computer"), converts the user's spoken input into text using OpenAI Whisper (speech to text), and generates responses through the ChatGPT API.

## Design

1. **User Interaction:**
   - The user asks a question using their microphone.

2. **Process Flow:**
   - **Recording the Audio (Step 1):**
     - **Input:**
       - Parameters: audio_queue, energy, pause, dynamic_energy.
     - **Process:**
       - Utilizes SpeechRecognition to create a recognizer.
       - Infinite loop captures and converts audio to PyTorch tensor.
       - Normalizes and stores tensor in audio_queue.
     - **Output:**
       - Recorded audio in PyTorch tensor format is placed in audio_queue.

   - **Transcribe the Audio (Step 2):**
     - **Input:**
       - Parameters: audio_queue, result_queue, audio_model, english, wake_word, verbose.
     - **Process:**
       - Retrieves audio data from audio_queue.
       - Transcribes audio using audio_model with language detection or English transcription based on the english flag.
       - Extracts and processes the transcribed text, removing the specified wake_word and punctuation.
       - If verbose, prints a message about wake word detection and text processing.
       - Adds the processed text to result_queue.
     - **Output:**
       - Processed text is stored in result_queue.

   - **Replying to User Request (Step 3):**
     - **Input:**
       - Parameter: result_queue.
     - **Process:**
       - Retrieves result from result_queue.
       - Language Model Call: Uses OpenAI's language model (Davinci) to generate a response.
       - Text-to-Speech Conversion: Converts the generated response to an audio file using gTTS.
       - Saves the audio as "reply.mp3."
       - Audio Playback: Plays back the "reply.mp3" file.
       - File Cleanup: Deletes "reply.mp3."
     - **Output:**
       - Generates and plays back an audio response from ChatGPT.

## Implementation Steps in Detail

### Step 1: Recording the Audio
- **Input:**
  - Parameters: audio_queue, energy, pause, dynamic_energy.
- **Process:**
  - Utilizes SpeechRecognition to create a recognizer.
  - Infinite loop captures and converts audio to PyTorch tensor.
  - Normalizes and stores tensor in audio_queue.
- **Output:**
  - Recorded audio in PyTorch tensor format is placed in audio_queue.

### Step 2: Transcribe the Audio
- **Input:**
  - Parameters: audio_queue, result_queue, audio_model, english, wake_word, verbose.
- **Process:**
  - Retrieves audio data from audio_queue.
  - Transcribes audio using audio_model with language detection or English transcription based on the english flag.
  - Extracts and processes the transcribed text, removing the specified wake_word and punctuation.
  - If verbose, prints a message about wake word detection and text processing.
  - Adds the processed text to result_queue.
- **Output:**
  - Processed text is stored in result_queue.

### Step 3: Replying to User Request
- **Input:**
  - Parameter: result_queue.
- **Process:**
  - Retrieves result from result_queue.
  - Language Model Call: Uses OpenAI's language model (Davinci) to generate a response.
  - Text-to-Speech Conversion: Converts the generated response to an audio file using gTTS.
  - Saves the audio as "reply.mp3."
  - Audio Playback: Plays back the "reply.mp3" file.
  - File Cleanup: Deletes "reply.mp3."
- **Output:**
  - Generates and plays back an audio response from ChatGPT.

## Installation

Install the following supported packages:

```bash
pip install pydub pyaudio speechrecognition whisper torch numpy gtts openai click
```

## Running the Script

```bash
python3 my_app.py
```

Ask a question. It continuously listens and wakes the system using the "hey Computer" wake word. If you want to stop, say "stop." The output is available in response.txt and a .mp3 (speech) file.

## Test

<img width="608" alt="Screen Shot 2023-11-15 at 12 57 35 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/cd619c05-46bd-4454-8f9f-d6fd40e5e636">
<img width="639" alt="Screen Shot 2023-11-15 at 1 18 35 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/07c99753-3c4f-481c-b78d-c3215e4f7abe">
