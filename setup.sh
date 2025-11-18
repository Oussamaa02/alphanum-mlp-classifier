#!/bin/bash

# Setup script for local development

echo "🚀 Setting up Alphanum MLP Classifier for local development..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 14 or higher."
    exit 1
fi

echo "✅ Node.js found: $(node --version)"
echo ""

# Setup backend
echo "📦 Setting up backend..."
cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate || . venv/Scripts/activate

echo "Installing backend dependencies..."
pip install -r requirements.txt

echo "✅ Backend setup complete!"
echo ""
cd ..

# Setup frontend
echo "📦 Setting up frontend..."
cd frontend

echo "Installing frontend dependencies..."
npm install --legacy-peer-deps

echo "✅ Frontend setup complete!"
echo ""
cd ..

# Create .env files if they don't exist
if [ ! -f "frontend/.env" ]; then
    echo "Creating frontend/.env from .env.example..."
    cp frontend/.env.example frontend/.env
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the application:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd backend"
echo "  source venv/bin/activate  # On Windows: venv\\Scripts\\activate"
echo "  python app.py"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "Then open http://localhost:3000 in your browser!"
echo ""
echo "For deployment instructions, see DEPLOYMENT.md"
