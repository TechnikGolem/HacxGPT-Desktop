# Changelog

All notable changes to the HacxGPT Desktop project will be documented in this file.

> **📝 Note**: This project is based on BlackTechX's original HacxGPT CLI and enhanced with desktop GUI features by TechnikGolem.

## [2.0.0] - 2025-10-21 - Desktop GUI Release

### 🆕 Added
- **Desktop GUI Interface** using PyQt6 (enhancement from original CLI)
- **Multi-Theme Support** (Cyberpunk, Matrix, Gaming, Modern)
- **Built-in Hacker Tools**:
  - Port Scanner with threading
  - Hash Generator (MD5, SHA1, SHA256, SHA512)
  - Base64 Encoder/Decoder
  - Network Information Lookup
- **Multiple AI Provider Support**:
  - Groq (free 14.4k requests/day)
  - Together AI (free $25 credits)
  - Replicate (free $10 credits)
  - OpenRouter, DeepSeek, Anthropic
- **Free Provider Guide** with setup instructions
- **Standalone Executable** builds (.exe)
- **Configuration Management** (themes, settings persistence)
- **Improved Error Handling** with helpful suggestions
- **Streaming Chat Interface** with real-time responses

### 🔧 Enhanced
- **Better API Error Messages** with provider recommendations
- **Smart Provider Selection** (Groq prioritized for free usage)
- **Professional UI Design** with customizable themes
- **Responsive Layout** with sidebar navigation

### 🐛 Fixed
- Removed problematic Hugging Face API integration
- Fixed CSS compatibility issues with PyQt6
- Improved stability for long-running chat sessions
- Better handling of API rate limits

### 📦 Build System
- Added PyInstaller configuration
- Created automated build scripts
- Version information embedding
- Icon and resource management

## [1.0.0] - Original

### Base Features (by BlackTechX)
- **CLI Interface** with Rich formatting
- **OpenRouter & DeepSeek** API support
- **Uncensored AI** conversation capabilities
- **Basic chat functionality**
- **API key management**

---

## [1.0.0] - 2024 - Original CLI Foundation

### 🏗️ Foundation (by BlackTechX)
- **Command Line Interface** for AI interactions
- **OpenAI API Integration** 
- **Basic chat functionality**
- **Configuration system**
- **Cross-platform compatibility**
- **Open source release** under CC BY-NC-SA 4.0

### 📝 Attribution
- **Original Creator**: BlackTechX ([github.com/BlackTechX011](https://github.com/BlackTechX011))
- **Original Repository**: [HacxGPT CLI](https://github.com/BlackTechX011/Hacx-GPT)
- **Foundation**: This version formed the base for the desktop enhancement

---

## Version Naming

- **v1.x**: Original CLI version by BlackTechX
- **v2.x**: Desktop GUI enhancement with additional features
- **v2.0.0**: Initial desktop release
- **v2.0.1**: Bug fixes and improvements (planned)
- **v2.1.0**: Additional features (planned)

## Credits

- **🏠 Original Project**: BlackTechX's HacxGPT CLI
- **🖥️ Desktop Enhancement**: TechnikGolem (taken from colleague with attribution)
- **🤝 Collaboration**: Maintaining respect for original creator while adding new features