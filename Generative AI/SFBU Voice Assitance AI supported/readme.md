# SFBU Voice Assistance AI Supported

## Introduction

This project aims to create a sophisticated voice-activated conversational system tailored for customer support. The question-answers are derived from a customer-provided document. The system integrates advanced technologies in audio processing, speech recognition, conversational AI, and document context processing. It operates by listening for a specific wake word, processing spoken queries or commands, and generating contextually relevant responses based on information from a loaded document. This voice assistant is well-suited for applications such as interactive voice assistants, automated customer support, or educational tools, where accessing document-based information through voice commands is valuable.

## Design

### Step 1: SFBU Customer Support System - Text Processing

- Implemented separately SFBU Customer Support System using Vector store and Embedding.

### Step 2: Real-time Speech to Text to Speech

- Implement Real-time Speech to Text to Speech using OpenAI-Whisper and API for speech-to-text conversion.

### Step 3: Integration of Steps 1 and 2

- Enhance Step 2 by adding the features implemented in Step 1.
- Two approaches to add the features:
  - **Option 1: Hard-coding the features on Step 2 (Used for this application).**
  - Option 2: Using a library.
  - Instead of hard-coding the features on Step 2, a better idea is to implement the features as libraries that can be used for both Step 1 and Step 2.

## Implementation Steps

### Install the following supported packages:

```bash
pip install pydub pyaudio speechrecognition whisper torch numpy gtts openai click
```

### Run the Script

```bash
python3 my_app.py
```

Ask questions based on the University SFBU Catalog. The system continuously listens and responds to the wake word "hey Computer." To stop the application, say "stop." The output is available in response.txt and a .mp3 (speech) file.

## Test
<img width="635" alt="Screen Shot 2023-11-15 at 1 17 08 AM" src="https://github.com/DKruti/Machine-Learning/assets/120690177/734ef5f3-c059-4e26-a0b6-a714efeeebbb">

