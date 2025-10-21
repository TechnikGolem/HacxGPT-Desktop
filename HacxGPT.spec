# -*- mode: python ; coding: utf-8 -*-
# HacxGPT Desktop - PyInstaller Specification File
# Builds both CLI and GUI versions

a = Analysis(
    ['HacxGPT_GUI.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icon.ico', '.'),
    ],
    hiddenimports=[
        'PyQt6.QtCore', 
        'PyQt6.QtWidgets', 
        'PyQt6.QtGui',
        'socket',
        'hashlib',
        'base64',
        'threading'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='HacxGPT',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
    version='version_info.txt'
)