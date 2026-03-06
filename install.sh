#!/bin/bash

echo "Installing Python dependencies..."

pip install -r requirements.txt

echo "Setup complete."

echo "Set environment variable:"
echo "export TUSHARE_TOKEN=your_token"
