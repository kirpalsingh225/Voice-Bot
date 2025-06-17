#!/usr/bin/env bash

# Install system dependencies for pyttsx3 (eSpeak) and PyAudio
apt-get update && apt-get install -y \
    espeak \
    libespeak-dev \
    portaudio19-dev

# Install Python dependencies
pip install -r requirements.txt
