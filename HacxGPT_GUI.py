#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HacxGPT Desktop GUI - Multi-Theme Advanced Interface
Created by: Enhanced by AI Assistant
Based on: BlackTechX's HacxGPT
"""

import sys
import os
import json
import time
import socket
import hashlib
import base64
import subprocess
import threading
from typing import Dict, Any, Optional
from pathlib import Path

try:
    from PyQt6.QtWidgets import *
    from PyQt6.QtCore import *
    from PyQt6.QtGui import *
    import openai
    from dotenv import load_dotenv, set_key
except ImportError:
    print("Installing required packages...")
    os.system(f'{sys.executable} -m pip install PyQt6 openai python-dotenv')
    print("Dependencies installed. Please restart the application.")
    sys.exit(0)

# --- Themes Configuration ---
class Themes:
    CYBERPUNK = {
        "name": "Cyberpunk",
        "primary": "#00ff41",
        "secondary": "#ff0080", 
        "background": "#0a0a0a",
        "surface": "#1a1a1a",
        "text": "#00ff41",
        "accent": "#ff0080",
        "button": "#2a2a2a",
        "hover": "#3a3a3a",
        "border": "#00ff41",
        "gradient": "linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%)",
        "glow": "0px 0px 10px #00ff41"
    }
    
    MATRIX = {
        "name": "Matrix Hacker",
        "primary": "#00ff00",
        "secondary": "#008000",
        "background": "#000000", 
        "surface": "#001100",
        "text": "#00ff00",
        "accent": "#00aa00",
        "button": "#002200",
        "hover": "#003300",
        "border": "#00ff00",
        "gradient": "linear-gradient(135deg, #000000 0%, #001100 100%)",
        "glow": "0px 0px 8px #00ff00"
    }
    
    GAMING = {
        "name": "Gaming RGB",
        "primary": "#ff6b6b",
        "secondary": "#4ecdc4",
        "background": "#1e1e1e",
        "surface": "#2d2d2d", 
        "text": "#ffffff",
        "accent": "#ff6b6b",
        "button": "#3d3d3d",
        "hover": "#4d4d4d",
        "border": "#ff6b6b",
        "gradient": "linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 50%, #1e1e1e 100%)",
        "glow": "0px 0px 15px #ff6b6b"
    }
    
    MODERN = {
        "name": "Modern Clean",
        "primary": "#007acc",
        "secondary": "#005a9e",
        "background": "#f5f5f5",
        "surface": "#ffffff",
        "text": "#333333",
        "accent": "#007acc", 
        "button": "#e0e0e0",
        "hover": "#d0d0d0",
        "border": "#cccccc",
        "gradient": "linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%)",
        "glow": "0px 0px 5px #007acc"
    }

# --- Hacker Tools Module ---
class HackerTools:
    @staticmethod
    def port_scanner(target: str, start_port: int = 1, end_port: int = 1000) -> Dict[int, str]:
        """Scannt Ports auf einem Ziel-Host"""
        open_ports = {}
        
        def scan_port(host, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "unknown"
                    open_ports[port] = service
                sock.close()
            except:
                pass
        
        threads = []
        for port in range(start_port, min(end_port + 1, 65536)):
            thread = threading.Thread(target=scan_port, args=(target, port))
            threads.append(thread)
            thread.start()
            
            # Limit concurrent threads
            if len(threads) >= 100:
                for t in threads:
                    t.join()
                threads = []
        
        # Wait for remaining threads
        for thread in threads:
            thread.join()
            
        return open_ports
    
    @staticmethod
    def hash_generator(text: str, algorithms: list = None) -> Dict[str, str]:
        """Generiert verschiedene Hash-Werte"""
        if algorithms is None:
            algorithms = ['md5', 'sha1', 'sha256', 'sha512']
        
        hashes = {}
        text_bytes = text.encode('utf-8')
        
        for algo in algorithms:
            try:
                if algo == 'md5':
                    hashes[algo] = hashlib.md5(text_bytes).hexdigest()
                elif algo == 'sha1':
                    hashes[algo] = hashlib.sha1(text_bytes).hexdigest()
                elif algo == 'sha256':
                    hashes[algo] = hashlib.sha256(text_bytes).hexdigest()
                elif algo == 'sha512':
                    hashes[algo] = hashlib.sha512(text_bytes).hexdigest()
            except:
                hashes[algo] = "Error"
        
        return hashes
    
    @staticmethod
    def base64_encode(text: str) -> str:
        """Base64 Encoding"""
        try:
            return base64.b64encode(text.encode('utf-8')).decode('utf-8')
        except:
            return "Encoding Error"
    
    @staticmethod
    def base64_decode(encoded: str) -> str:
        """Base64 Decoding"""
        try:
            return base64.b64decode(encoded.encode('utf-8')).decode('utf-8')
        except:
            return "Decoding Error"
    
    @staticmethod
    def ip_info(target: str) -> Dict[str, str]:
        """Sammelt IP-Informationen"""
        info = {}
        try:
            # DNS Lookup
            info['hostname'] = socket.gethostbyaddr(target)[0]
        except:
            info['hostname'] = "Unknown"
        
        try:
            # IP Address
            info['ip'] = socket.gethostbyname(target)
        except:
            info['ip'] = target
        
        return info
    
    @staticmethod
    def whois_lookup(domain: str) -> str:
        """Whois Lookup (Windows)"""
        try:
            result = subprocess.run(['nslookup', domain], 
                                  capture_output=True, text=True, timeout=10)
            return result.stdout
        except:
            return "Whois lookup failed"

# --- Hacker Tools Dialog ---
class HackerToolsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("🔥 HacxGPT - Hacker Tools")
        self.setFixedSize(800, 600)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Tab Widget for different tools
        self.tab_widget = QTabWidget()
        
        # Port Scanner Tab
        self.create_port_scanner_tab()
        
        # Hash Generator Tab
        self.create_hash_generator_tab()
        
        # Base64 Tools Tab
        self.create_base64_tab()
        
        # Network Info Tab
        self.create_network_info_tab()
        
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)
    
    def create_port_scanner_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Input section
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Target:"))
        self.target_input = QLineEdit("127.0.0.1")
        input_layout.addWidget(self.target_input)
        
        input_layout.addWidget(QLabel("Ports:"))
        self.start_port = QSpinBox()
        self.start_port.setRange(1, 65535)
        self.start_port.setValue(1)
        input_layout.addWidget(self.start_port)
        
        input_layout.addWidget(QLabel("bis"))
        self.end_port = QSpinBox()
        self.end_port.setRange(1, 65535)
        self.end_port.setValue(1000)
        input_layout.addWidget(self.end_port)
        
        self.scan_btn = QPushButton("🎯 Scan starten")
        self.scan_btn.clicked.connect(self.run_port_scan)
        input_layout.addWidget(self.scan_btn)
        
        layout.addLayout(input_layout)
        
        # Results
        self.port_results = QTextEdit()
        self.port_results.setReadOnly(True)
        layout.addWidget(self.port_results)
        
        tab.setLayout(layout)
        self.tab_widget.addTab(tab, "🎯 Port Scanner")
    
    def create_hash_generator_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Input
        layout.addWidget(QLabel("Text zum Hashen:"))
        self.hash_input = QTextEdit()
        self.hash_input.setMaximumHeight(100)
        layout.addWidget(self.hash_input)
        
        # Buttons
        btn_layout = QHBoxLayout()
        self.hash_btn = QPushButton("🔒 Hashes generieren")
        self.hash_btn.clicked.connect(self.generate_hashes)
        btn_layout.addWidget(self.hash_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        # Results
        self.hash_results = QTextEdit()
        self.hash_results.setReadOnly(True)
        layout.addWidget(self.hash_results)
        
        tab.setLayout(layout)
        self.tab_widget.addTab(tab, "🔒 Hash Generator")
    
    def create_base64_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Input
        layout.addWidget(QLabel("Text:"))
        self.base64_input = QTextEdit()
        self.base64_input.setMaximumHeight(150)
        layout.addWidget(self.base64_input)
        
        # Buttons
        btn_layout = QHBoxLayout()
        encode_btn = QPushButton("📤 Encode")
        decode_btn = QPushButton("📥 Decode")
        encode_btn.clicked.connect(self.base64_encode)
        decode_btn.clicked.connect(self.base64_decode)
        btn_layout.addWidget(encode_btn)
        btn_layout.addWidget(decode_btn)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)
        
        # Results
        layout.addWidget(QLabel("Ergebnis:"))
        self.base64_results = QTextEdit()
        self.base64_results.setMaximumHeight(150)
        layout.addWidget(self.base64_results)
        
        tab.setLayout(layout)
        self.tab_widget.addTab(tab, "📦 Base64 Tools")
    
    def create_network_info_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Input
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Domain/IP:"))
        self.network_input = QLineEdit("google.com")
        input_layout.addWidget(self.network_input)
        
        lookup_btn = QPushButton("🔍 Lookup")
        lookup_btn.clicked.connect(self.network_lookup)
        input_layout.addWidget(lookup_btn)
        
        layout.addLayout(input_layout)
        
        # Results
        self.network_results = QTextEdit()
        self.network_results.setReadOnly(True)
        layout.addWidget(self.network_results)
        
        tab.setLayout(layout)
        self.tab_widget.addTab(tab, "🌐 Network Info")
    
    def run_port_scan(self):
        target = self.target_input.text()
        start = self.start_port.value()
        end = self.end_port.value()
        
        self.port_results.setText("🎯 Scanning ports... Please wait...")
        self.scan_btn.setEnabled(False)
        
        # Run in thread to avoid blocking UI
        def scan_thread():
            try:
                results = HackerTools.port_scanner(target, start, end)
                
                if results:
                    output = f"🎯 Open Ports on {target}:\n\n"
                    for port, service in sorted(results.items()):
                        output += f"Port {port}: {service}\n"
                else:
                    output = f"❌ No open ports found on {target} (Range: {start}-{end})"
                
                # Update UI in main thread
                QTimer.singleShot(0, lambda: self.update_port_results(output))
            except Exception as e:
                QTimer.singleShot(0, lambda: self.update_port_results(f"❌ Error: {str(e)}"))
        
        threading.Thread(target=scan_thread, daemon=True).start()
    
    def update_port_results(self, text):
        self.port_results.setText(text)
        self.scan_btn.setEnabled(True)
    
    def generate_hashes(self):
        text = self.hash_input.toPlainText()
        if not text:
            self.hash_results.setText("❌ Bitte Text eingeben!")
            return
        
        hashes = HackerTools.hash_generator(text)
        
        output = f"🔒 Hash-Werte für: '{text}'\n\n"
        for algo, hash_value in hashes.items():
            output += f"{algo.upper()}: {hash_value}\n"
        
        self.hash_results.setText(output)
    
    def base64_encode(self):
        text = self.base64_input.toPlainText()
        if not text:
            self.base64_results.setText("❌ Bitte Text eingeben!")
            return
        
        encoded = HackerTools.base64_encode(text)
        self.base64_results.setText(encoded)
    
    def base64_decode(self):
        text = self.base64_input.toPlainText()
        if not text:
            self.base64_results.setText("❌ Bitte Text eingeben!")
            return
        
        decoded = HackerTools.base64_decode(text)
        self.base64_results.setText(decoded)
    
    def network_lookup(self):
        target = self.network_input.text()
        if not target:
            return
        
        self.network_results.setText("🔍 Looking up information...")
        
        def lookup_thread():
            try:
                # IP Info
                ip_info = HackerTools.ip_info(target)
                
                # Whois
                whois_info = HackerTools.whois_lookup(target)
                
                output = f"🌐 Network Information for: {target}\n\n"
                output += f"Hostname: {ip_info.get('hostname', 'Unknown')}\n"
                output += f"IP Address: {ip_info.get('ip', 'Unknown')}\n\n"
                output += "📋 DNS Lookup Results:\n"
                output += whois_info
                
                QTimer.singleShot(0, lambda: self.network_results.setText(output))
            except Exception as e:
                QTimer.singleShot(0, lambda: self.network_results.setText(f"❌ Error: {str(e)}"))
        
        threading.Thread(target=lookup_thread, daemon=True).start()

# --- Configuration Management ---
class Config:
    CONFIG_FILE = Path(".hacx_gui_config.json")
    ENV_FILE = ".hacx"
    
    # API Providers
    PROVIDERS = {
        "openrouter": {
            "BASE_URL": "https://openrouter.ai/api/v1",
            "MODEL_NAME": "deepseek/deepseek-chat-v3-0324:free",
        },
        "deepseek": {
            "BASE_URL": "https://api.deepseek.com", 
            "MODEL_NAME": "deepseek-chat",
        },
        "anthropic": {
            "BASE_URL": "https://api.anthropic.com",
            "MODEL_NAME": "claude-3-haiku-20240307",
        },
        "huggingface": {
            "BASE_URL": "https://api-inference.huggingface.co/models",
            "MODEL_NAME": "microsoft/DialoGPT-medium",
            "HEADERS": {"Authorization": "Bearer "},
            "TYPE": "huggingface"
        },
        "groq": {
            "BASE_URL": "https://api.groq.com/openai/v1",
            "MODEL_NAME": "llama-3.1-70b-versatile",
        },
        "together": {
            "BASE_URL": "https://api.together.xyz/v1",
            "MODEL_NAME": "meta-llama/Llama-3-70b-chat-hf",
        },
        "replicate": {
            "BASE_URL": "https://api.replicate.com/v1",
            "MODEL_NAME": "meta/llama-2-70b-chat",
        }
    }
    
    DEFAULT_CONFIG = {
        "theme": "CYBERPUNK",
        "api_provider": "openrouter",
        "window_size": [1200, 800],
        "font_size": 12,
        "animations": True,
        "sound": False,
        "transparency": 0.95
    }
    
    @classmethod
    def load_config(cls) -> Dict[str, Any]:
        if cls.CONFIG_FILE.exists():
            try:
                with open(cls.CONFIG_FILE, 'r', encoding='utf-8') as f:
                    return {**cls.DEFAULT_CONFIG, **json.load(f)}
            except:
                pass
        return cls.DEFAULT_CONFIG.copy()
    
    @classmethod
    def save_config(cls, config: Dict[str, Any]):
        with open(cls.CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)

# --- API Client ---
class LLMClient(QObject):
    response_received = pyqtSignal(str)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, api_key: str, provider: str):
        super().__init__()
        self.api_key = api_key
        self.provider = provider
        self.history = []
        self._init_client()
        
    def _init_client(self):
        provider_config = Config.PROVIDERS[self.provider]
        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url=provider_config["BASE_URL"]
        )
        self.model_name = provider_config["MODEL_NAME"]
        self._reset_history()
    
    def _reset_history(self):
        system_prompt = """
        You are HacxGPT, an advanced AI assistant created by BlackTechX. 
        You are helpful, knowledgeable, and direct in your responses.
        Always respond in the user's language and provide detailed, accurate information.
        """
        self.history = [{"role": "system", "content": system_prompt}]
    
    def send_message(self, message: str):
        self.history.append({"role": "user", "content": message})
        
        try:
            # Check for problematic providers
            if self.provider == "huggingface":
                self.error_occurred.emit("❌ Hugging Face hat API-Probleme. Nutze GROQ stattdessen! (Kostenlose APIs Button für Anleitung)")
                self.history.pop()
                return
                
            # Standard OpenAI-compatible API
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self.history,
                temperature=0.7,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            self.history.append({"role": "assistant", "content": content})
            self.response_received.emit(content)
            
        except Exception as e:
            error_msg = str(e)
            
            # Better error messages
            if "403" in error_msg:
                error_msg = "❌ API-Key Fehler: Keine Berechtigung. Versuche GROQ (kostenlos & zuverlässig)!"
            elif "401" in error_msg:
                error_msg = "❌ API-Key ungültig. Bitte neuen Key erstellen oder GROQ probieren."
            elif "429" in error_msg:
                error_msg = "❌ Rate-Limit erreicht. Warte kurz oder wechsel zu GROQ."
            elif "insufficient" in error_msg.lower():
                error_msg = "❌ Provider-Problem. GROQ ist der beste kostenlose Provider!"
            else:
                error_msg = f"❌ Fehler: {error_msg}\n\n💡 Tipp: GROQ ist kostenlos und funktioniert immer!"
            
            self.error_occurred.emit(error_msg)
            self.history.pop()  # Remove failed user message
    
    def clear_history(self):
        self._reset_history()

# --- Settings Dialog ---
class SettingsDialog(QDialog):
    def __init__(self, config: Dict[str, Any], parent=None):
        super().__init__(parent)
        self.config = config.copy()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("HacxGPT - Einstellungen")
        self.setFixedSize(500, 600)
        
        layout = QVBoxLayout()
        
        # Theme Selection
        theme_group = QGroupBox("Theme")
        theme_layout = QVBoxLayout()
        
        self.theme_combo = QComboBox()
        themes = ["CYBERPUNK", "MATRIX", "GAMING", "MODERN"]
        self.theme_combo.addItems(themes)
        self.theme_combo.setCurrentText(self.config["theme"])
        theme_layout.addWidget(self.theme_combo)
        theme_group.setLayout(theme_layout)
        
        # API Provider
        api_group = QGroupBox("API Provider")
        api_layout = QVBoxLayout()
        
        self.api_combo = QComboBox()
        self.api_combo.addItems(["groq", "openrouter", "deepseek", "anthropic", "together", "replicate"])
        self.api_combo.setCurrentText(self.config["api_provider"])
        api_layout.addWidget(self.api_combo)
        api_group.setLayout(api_layout)
        
        # Font Size
        font_group = QGroupBox("Schriftgröße")
        font_layout = QVBoxLayout()
        
        self.font_slider = QSlider(Qt.Orientation.Horizontal)
        self.font_slider.setRange(8, 24)
        self.font_slider.setValue(self.config["font_size"])
        self.font_label = QLabel(f"Größe: {self.config['font_size']}px")
        self.font_slider.valueChanged.connect(
            lambda v: self.font_label.setText(f"Größe: {v}px")
        )
        
        font_layout.addWidget(self.font_label)
        font_layout.addWidget(self.font_slider)
        font_group.setLayout(font_layout)
        
        # Transparency
        trans_group = QGroupBox("Transparenz")
        trans_layout = QVBoxLayout()
        
        self.trans_slider = QSlider(Qt.Orientation.Horizontal)
        self.trans_slider.setRange(50, 100)
        self.trans_slider.setValue(int(self.config["transparency"] * 100))
        self.trans_label = QLabel(f"Transparenz: {int(self.config['transparency'] * 100)}%")
        self.trans_slider.valueChanged.connect(
            lambda v: self.trans_label.setText(f"Transparenz: {v}%")
        )
        
        trans_layout.addWidget(self.trans_label)
        trans_layout.addWidget(self.trans_slider)
        trans_group.setLayout(trans_layout)
        
        # Checkboxes
        self.animations_check = QCheckBox("Animationen aktivieren")
        self.animations_check.setChecked(self.config["animations"])
        
        self.sound_check = QCheckBox("Sound-Effekte")
        self.sound_check.setChecked(self.config["sound"])
        
        # Buttons
        button_layout = QHBoxLayout()
        save_btn = QPushButton("Speichern")
        cancel_btn = QPushButton("Abbrechen")
        
        save_btn.clicked.connect(self.save_settings)
        cancel_btn.clicked.connect(self.reject)
        
        button_layout.addWidget(save_btn)
        button_layout.addWidget(cancel_btn)
        
        # Add all to main layout
        layout.addWidget(theme_group)
        layout.addWidget(api_group)
        layout.addWidget(font_group)
        layout.addWidget(trans_group)
        layout.addWidget(self.animations_check)
        layout.addWidget(self.sound_check)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def save_settings(self):
        self.config.update({
            "theme": self.theme_combo.currentText(),
            "api_provider": self.api_combo.currentText(),
            "font_size": self.font_slider.value(),
            "transparency": self.trans_slider.value() / 100,
            "animations": self.animations_check.isChecked(),
            "sound": self.sound_check.isChecked()
        })
        self.accept()

# --- Main GUI ---
class HacxGPTGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = Config.load_config()
        self.llm_client = None
        self.init_ui()
        self.apply_theme()
        
    def init_ui(self):
        self.setWindowTitle("HacxGPT - Advanced AI Interface")
        self.setGeometry(100, 100, *self.config["window_size"])
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        
        # Left sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar, 1)
        
        # Right chat area
        chat_area = self.create_chat_area()
        main_layout.addWidget(chat_area, 4)
        
        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("HacxGPT bereit - API-Key konfigurieren")
        
    def create_sidebar(self):
        sidebar = QWidget()
        sidebar.setFixedWidth(250)
        layout = QVBoxLayout(sidebar)
        
        # Logo/Title
        title = QLabel("HacxGPT")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        
        # Buttons
        self.connect_btn = QPushButton("🔑 API verbinden")
        self.free_setup_btn = QPushButton("🆓 Kostenlose APIs")
        self.new_chat_btn = QPushButton("💬 Neuer Chat")
        self.hacker_tools_btn = QPushButton("💀 Hacker Tools")
        self.settings_btn = QPushButton("⚙️ Einstellungen")
        self.about_btn = QPushButton("ℹ️ Über")
        
        # Connect signals
        self.connect_btn.clicked.connect(self.configure_api)
        self.free_setup_btn.clicked.connect(self.show_free_apis)
        self.new_chat_btn.clicked.connect(self.new_chat)
        self.hacker_tools_btn.clicked.connect(self.open_hacker_tools)
        self.settings_btn.clicked.connect(self.open_settings)
        self.about_btn.clicked.connect(self.show_about)
        
        # Add to layout
        layout.addWidget(title)
        layout.addWidget(self.connect_btn)
        layout.addWidget(self.free_setup_btn)
        layout.addWidget(self.new_chat_btn)
        layout.addWidget(self.hacker_tools_btn)
        layout.addWidget(self.settings_btn)
        layout.addWidget(self.about_btn)
        layout.addStretch()
        
        return sidebar
    
    def create_chat_area(self):
        chat_widget = QWidget()
        layout = QVBoxLayout(chat_widget)
        
        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display, 1)
        
        # Input area
        input_layout = QHBoxLayout()
        
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Nachricht eingeben...")
        self.message_input.returnPressed.connect(self.send_message)
        
        self.send_btn = QPushButton("Senden")
        self.send_btn.clicked.connect(self.send_message)
        
        input_layout.addWidget(self.message_input, 1)
        input_layout.addWidget(self.send_btn)
        
        layout.addLayout(input_layout)
        
        return chat_widget
    
    def apply_theme(self):
        theme_name = self.config["theme"]
        theme = getattr(Themes, theme_name)
        
        # Main window style
        style = f"""
        QMainWindow {{
            background: {theme['gradient']};
            color: {theme['text']};
        }}
        
        QWidget {{
            background-color: {theme['background']};
            color: {theme['text']};
            font-size: {self.config['font_size']}px;
        }}
        
        QPushButton {{
            background-color: {theme['button']};
            border: 2px solid {theme['border']};
            border-radius: 8px;
            padding: 10px;
            color: {theme['text']};
            font-weight: bold;
        }}
        
        QPushButton:hover {{
            background-color: {theme['hover']};
        }}
        
        QTextEdit {{
            background-color: {theme['surface']};
            border: 1px solid {theme['border']};
            border-radius: 8px;
            padding: 10px;
            color: {theme['text']};
        }}
        
        QLineEdit {{
            background-color: {theme['surface']};
            border: 2px solid {theme['border']};
            border-radius: 8px;
            padding: 8px;
            color: {theme['text']};
        }}
        
        QLabel {{
            color: {theme['text']};
        }}
        
        QStatusBar {{
            background-color: {theme['surface']};
            color: {theme['text']};
            border-top: 1px solid {theme['border']};
        }}
        """
        
        self.setStyleSheet(style)
        self.setWindowOpacity(self.config["transparency"])
    
    def show_free_apis(self):
        """Zeigt Guide für kostenlose API-Provider"""
        free_apis_text = """
<h2>🆓 Kostenlose AI-Provider</h2>

<h3>🚀 EMPFEHLUNG: Groq (Bester kostenloser Provider!)</h3>
<p><b>✅ Groq:</b> 14.400 Requests/Tag, Ultra-schnell<br>
   → <a href="https://console.groq.com/">console.groq.com</a><br>
   → Erstelle Account → API Keys → Key kopieren<br>
   → Zurück zu HacxGPT → Einstellungen → Provider: "groq"</p>

<h3>🆓 Alternative kostenlose Provider:</h3>
<ol>
<li><b>Together AI</b> - $25 Start-Credits<br>
   → <a href="https://api.together.xyz/">api.together.xyz</a></li>
<li><b>Replicate</b> - $10 Start-Credits<br>
   → <a href="https://replicate.com/">replicate.com</a></li>
</ol>

<h3>⚠️ Hugging Face Problem:</h3>
<p>Hugging Face hat API-Permission-Probleme.<br>
<b>Nutze stattdessen Groq - funktioniert sofort!</b></p>

<h3>💡 Quick Setup (Groq):</h3>
<p>1. https://console.groq.com/keys<br>
2. Account erstellen<br>
3. "Create API Key" klicken<br>
4. Key kopieren (beginnt mit "gsk_...")<br>
5. HacxGPT → Einstellungen → Provider: "groq"<br>
6. API verbinden → Key einfügen → Fertig!</p>

<p><b>🔥 Groq ist der beste kostenlose Provider:</b><br>
- Sehr schnell<br>
- Zuverlässig<br>
- Gute Modelle (Llama 3.1 70B)<br>
- 14.400 Requests/Tag</p>
        """
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("🆓 Kostenlose AI-Provider")
        msg_box.setTextFormat(Qt.TextFormat.RichText)
        msg_box.setText(free_apis_text)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
    
    def configure_api(self):
        api_key, ok = QInputDialog.getText(
            self, 
            "API-Konfiguration",
            f"API-Key für {self.config['api_provider']} eingeben:",
            QLineEdit.EchoMode.Password
        )
        
        if ok and api_key:
            try:
                # Save API key
                load_dotenv(dotenv_path=Config.ENV_FILE)
                set_key(Config.ENV_FILE, "HacxGPT-API", api_key)
                
                # Initialize client
                self.llm_client = LLMClient(api_key, self.config["api_provider"])
                self.llm_client.response_received.connect(self.display_response)
                self.llm_client.error_occurred.connect(self.display_error)
                
                self.status_bar.showMessage("✅ API erfolgreich verbunden!")
                self.connect_btn.setText("✅ Verbunden")
                
            except Exception as e:
                QMessageBox.warning(self, "Fehler", f"API-Verbindung fehlgeschlagen:\n{e}")
    
    def send_message(self):
        if not self.llm_client:
            QMessageBox.warning(self, "Fehler", "Bitte zuerst API-Key konfigurieren!")
            return
            
        message = self.message_input.text().strip()
        if not message:
            return
            
        # Display user message
        self.display_message("Du", message, "#4CAF50")
        self.message_input.clear()
        
        # Send to API
        self.llm_client.send_message(message)
        self.status_bar.showMessage("🤖 HacxGPT denkt...")
    
    def display_message(self, sender: str, message: str, color: str = "#FFFFFF"):
        timestamp = time.strftime("%H:%M:%S")
        formatted_message = f"""
        <div style="margin: 10px 0; padding: 10px; border-left: 3px solid {color};">
            <b style="color: {color};">[{timestamp}] {sender}:</b><br>
            <span style="margin-left: 10px;">{message}</span>
        </div>
        """
        self.chat_display.append(formatted_message)
    
    def display_response(self, response: str):
        self.display_message("HacxGPT", response, "#FF6B6B")
        self.status_bar.showMessage("✅ Antwort erhalten")
    
    def display_error(self, error: str):
        self.display_message("Fehler", error, "#F44336")
        self.status_bar.showMessage("❌ Fehler aufgetreten")
    
    def new_chat(self):
        if self.llm_client:
            self.llm_client.clear_history()
        self.chat_display.clear()
        self.status_bar.showMessage("🔄 Neuer Chat gestartet")
    
    def open_hacker_tools(self):
        """Öffnet das Hacker Tools Fenster"""
        dialog = HackerToolsDialog(self)
        dialog.exec()
    
    def open_settings(self):
        dialog = SettingsDialog(self.config, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.config = dialog.config
            Config.save_config(self.config)
            self.apply_theme()
            
            # Restart client if provider changed
            if self.llm_client:
                api_key = self.llm_client.api_key
                self.llm_client = LLMClient(api_key, self.config["api_provider"])
                self.llm_client.response_received.connect(self.display_response)
                self.llm_client.error_occurred.connect(self.display_error)
    
    def show_about(self):
        about_text = """
        <h2>HacxGPT Desktop GUI</h2>
        <p><b>Version:</b> 2.0 Enhanced</p>
        <p><b>Entwickelt von:</b> BlackTechX</p>
        <p><b>Enhanced by:</b> AI Assistant</p>
        <br>
        <p>Ein fortschrittliches AI-Interface mit Multi-Theme Support.</p>
        <p>Unterstützte Provider: OpenRouter, DeepSeek, Anthropic</p>
        <br>
        <p><b>Features:</b></p>
        <ul>
            <li>4 verschiedene Themes</li>
            <li>Anpassbare Oberfläche</li>
            <li>Multiple API-Provider</li>
            <li>Moderne Desktop-GUI</li>
        </ul>
        """
        
        QMessageBox.about(self, "Über HacxGPT", about_text)
    
    def closeEvent(self, event):
        # Save window size
        self.config["window_size"] = [self.width(), self.height()]
        Config.save_config(self.config)
        event.accept()

# --- Main Application ---
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("HacxGPT")
    app.setApplicationVersion("2.0")
    
    # Dark palette (fallback)
    app.setStyle('Fusion')
    
    window = HacxGPTGUI()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()