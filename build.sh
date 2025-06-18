#!/usr/bin/env bash

# Install only required system dependencies for your current setup
apt-get update && apt-get install -y \
    cmake \
    pkg-config

# Install Python dependencies
pip install -r requirements.txt
