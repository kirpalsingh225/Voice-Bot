#!/usr/bin/env bash
# Install system dependencies
apt-get update && apt-get install -y portaudio19-dev

# Continue with your usual build process
pip install -r requirements.txt
