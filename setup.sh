#!/bin/bash

# YouTube RAG App Setup Script
echo "🎥 YouTube RAG App Setup"
echo "========================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 is installed"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp .env.template .env
    echo "📝 Please edit .env file and add your PPLX_API_KEY"
    echo "   Get your API key from: https://www.perplexity.ai/settings/api"
else
    echo "✅ .env file exists"
fi

echo ""
echo "🚀 Setup complete!"
echo ""
echo "To run the app:"
echo "1. Make sure you've added your PPLX_API_KEY to the .env file"
echo "2. Run: streamlit run app.py"
echo ""
echo "To activate the virtual environment in the future:"
echo "   source venv/bin/activate"