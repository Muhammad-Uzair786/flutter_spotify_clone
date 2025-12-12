#!/bin/bash

# Change to the server directory
cd server

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m uvicorn main:app --host 0.0.0.0 --port $PORT
