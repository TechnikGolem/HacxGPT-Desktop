@echo off
echo ============================================
echo    HacxGPT Desktop - Professional Builder
echo    Building optimized executable...
echo ============================================

cd /d "%~dp0"

echo [1/5] Aktiviere Virtual Environment...
call .venv\Scripts\activate.bat

echo [2/5] Installiere/Update Dependencies...
pip install -r requirements.txt

echo [3/5] Bereinige alte Builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [4/5] Building mit optimierter Spec-Datei...
pyinstaller HacxGPT.spec

echo [5/5] Validierung und Finalisierung...
if exist "dist\HacxGPT.exe" (
    echo ============================================
    echo    ✅ BUILD ERFOLGREICH! 
    echo    📁 EXE Location: dist\HacxGPT.exe
    echo    📊 Size: 
    for %%F in (dist\HacxGPT.exe) do echo       %%~zF Bytes (%%~nF%%~xF)
    echo ============================================
    echo.
    echo 🚀 Die optimierte .exe ist bereit!
    echo 💻 Funktioniert auf jedem Windows-System
    echo 🔧 Alle Features inklusive (GUI + Hacker Tools)
    echo.
    echo Testen? (J/N)
    set /p test="➤ "
    if /i "%test%"=="J" (
        echo 🎯 Starte HacxGPT Desktop...
        start dist\HacxGPT.exe
    )
) else (
    echo ============================================
    echo    ❌ BUILD FEHLER!
    echo    🔍 Prüfe die Ausgabe oben für Details.
    echo ============================================
)

echo.
echo 📋 Build-Zusammenfassung:
echo    - Spec-Datei: HacxGPT.spec
echo    - Dependencies: requirements.txt
echo    - Icon: icon.ico
echo    - Version Info: version_info.txt
echo.
pause