#!/bin/bash
echo "Setting up environment for the application..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

cp .env.example .env

echo "Setup complete! Your environment is ready."
echo "To activate this environment in the future, run: source venv/bin/activate"