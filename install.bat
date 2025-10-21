@echo off
title HacxGPT Desktop Installer

echo ================================================
echo     HacxGPT Desktop - Complete Installation
echo ================================================
echo.
echo 🔧 Installing both CLI and GUI versions...
echo 💻 Desktop GUI with themes and hacker tools
echo 🔑 Multiple AI provider support
echo.

:: Check for Python
echo [1/6] Checking Python installation...
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python is nicht installiert oder nicht im PATH.
    echo 🔗 Installiere Python von: https://www.python.org/downloads/
    echo ⚠️  Stelle sicher, dass "Add Python to PATH" aktiviert ist!
    pause
    exit /b
)
echo ✅ Python gefunden.

:: Create virtual environment
echo [2/6] Erstelle Virtual Environment...
if not exist ".venv" (
    python -m venv .venv
    echo ✅ Virtual Environment erstellt.
) else (
    echo ✅ Virtual Environment bereits vorhanden.
)

:: Activate virtual environment
echo [3/6] Aktiviere Virtual Environment...
call .venv\Scripts\activate.bat

:: Install requirements
echo [4/6] Installiere Python Dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo ✅ Alle Dependencies installiert.

:: Create config files
echo [5/6] Erstelle Konfigurationsdateien...
if not exist ".hacx" (
    echo. > .hacx
)
if not exist ".hacx_gui_config.json" (
    echo {"theme": "cyberpunk", "provider": "groq"} > .hacx_gui_config.json
)
echo ✅ Konfiguration erstellt.

:: Test installation
echo [6/6] Teste Installation...
python -c "import PyQt6; import openai; print('✅ Alle Module verfügbar')" 2>nul
if %errorlevel% neq 0 (
    echo ⚠️  Warnung: Einige Module könnten fehlen
) else (
    echo ✅ Installation vollständig validiert.
)

echo.
echo ================================================
echo       🎉 INSTALLATION ERFOLGREICH! 🎉
echo ================================================
echo.
echo 🚀 Verfügbare Optionen:
echo    1. CLI Version:    python HacxGPT.py
echo    2. Desktop GUI:    python HacxGPT_GUI.py
echo    3. Build EXE:      build_exe.bat
echo.
echo 🔑 API Setup:
echo    - Kostenlose Provider: Siehe KOSTENLOSE_AI_PROVIDER.md
echo    - Empfohlen: Groq (gratis, schnell, zuverlässig)
echo.
echo 📚 Dokumentation: docs/README.md
echo ================================================
echo.
echo Möchtest du die Desktop GUI starten? (J/N)
set /p start="➤ "
if /i "%start%"=="J" (
    echo 🎯 Starte HacxGPT Desktop...
    python HacxGPT_GUI.py
)

pause
