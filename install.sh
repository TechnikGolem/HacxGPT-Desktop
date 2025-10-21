#!/bin/bash

# HacxGPT Desktop Installer for Linux and Termux
# https://github.com/BlackTechX011/Hacx-GPT

echo "=============================================="
echo "    HacxGPT Desktop - Complete Installation"
echo "=============================================="
echo ""
echo "🔧 Installing both CLI and GUI versions..."
echo "💻 Desktop GUI with themes and hacker tools"
echo "🔑 Multiple AI provider support"
echo ""

# Function to detect package manager
detect_pkg_manager() {
    if command -v apt-get &> /dev/null; then
        echo "apt"
    elif command -v pkg &> /dev/null; then
        echo "pkg"
    elif command -v yum &> /dev/null; then
        echo "yum"
    elif command -v dnf &> /dev/null; then
        echo "dnf"
    elif command -v pacman &> /dev/null; then
        echo "pacman"
    else
        echo "unknown"
    fi
}

PKG_MANAGER=$(detect_pkg_manager)

# Update and install dependencies
echo "[1/6] Updating package lists..."
if [ "$PKG_MANAGER" = "apt" ]; then
    sudo apt-get update -y
    echo "[2/6] Installing dependencies (git, python3, pip, PyQt6)..."
    sudo apt-get install git python3 python3-pip python3-venv python3-pyqt6 -y
elif [ "$PKG_MANAGER" = "pkg" ]; then
    pkg update -y
    echo "[2/6] Installing dependencies (git, python)..."
    pkg install git python -y
elif [ "$PKG_MANAGER" = "yum" ] || [ "$PKG_MANAGER" = "dnf" ]; then
    sudo $PKG_MANAGER update -y
    echo "[2/6] Installing dependencies..."
    sudo $PKG_MANAGER install git python3 python3-pip python3-venv -y
elif [ "$PKG_MANAGER" = "pacman" ]; then
    sudo pacman -Syu --noconfirm
    echo "[2/6] Installing dependencies..."
    sudo pacman -S git python python-pip python-virtualenv --noconfirm
else
    echo "❌ Unsupported package manager. Please install git, python3, and pip manually."
    exit 1
fi

# Create virtual environment
echo "[3/6] Creating virtual environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "✅ Virtual environment created."
else
    echo "✅ Virtual environment already exists."
fi

# Activate virtual environment
echo "[4/6] Activating virtual environment..."
source .venv/bin/activate

# Install Python requirements
echo "[5/6] Installing Python dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt
echo "✅ All dependencies installed."

# Create config files
echo "[6/6] Creating configuration files..."
if [ ! -f ".hacx" ]; then
    touch .hacx
fi
if [ ! -f ".hacx_gui_config.json" ]; then
    echo '{"theme": "cyberpunk", "provider": "groq"}' > .hacx_gui_config.json
fi
echo "✅ Configuration created."

# Test installation
echo ""
echo "Testing installation..."
python -c "import PyQt6; import openai; print('✅ All modules available')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Warning: Some modules might be missing"
else
    echo "✅ Installation fully validated."
fi

echo ""
echo "=============================================="
echo "       🎉 INSTALLATION SUCCESSFUL! 🎉"
echo "=============================================="
echo ""
echo "🚀 Available options:"
echo "   1. CLI Version:    python HacxGPT.py"
echo "   2. Desktop GUI:    python HacxGPT_GUI.py"
echo "   3. Build Binary:   See docs/building.md"
echo ""
echo "🔑 API Setup:"
echo "   - Free providers: See KOSTENLOSE_AI_PROVIDER.md"
echo "   - Recommended: Groq (free, fast, reliable)"
echo ""
echo "📚 Documentation: docs/README.md"
echo "=============================================="
echo ""
echo "Start Desktop GUI now? (y/n)"
read -p "➤ " start
if [ "$start" = "y" ] || [ "$start" = "Y" ]; then
    echo "🎯 Starting HacxGPT Desktop..."
    python HacxGPT_GUI.py
fi
