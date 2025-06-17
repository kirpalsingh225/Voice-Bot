#!/usr/bin/env bash

# Install system dependencies for PyAudio and pyttsx3
apt-get update && apt-get install -y \
    portaudio19-dev \
    espeak \
    libespeak-dev

# Continue with Python package install
pip install -r requirements.txt
