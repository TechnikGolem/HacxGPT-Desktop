# 🔥 HacxGPT - Advanced AI Desktop Interface

<div align="center">
  <img src="img/HacxGPT.png" alt="HacxGPT Logo" width="400"/>
  
  [![GitHub Stars](https://img.shields.io/github/stars/BlackTechX011/HacxGPT-Desktop?style=social)](https://github.com/BlackTechX011/HacxGPT-Desktop/stargazers)
  [![GitHub Forks](https://img.shields.io/github/forks/BlackTechX011/HacxGPT-Desktop?style=social)](https://github.com/BlackTechX011/HacxGPT-Desktop/network/members)
  [![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-red)](LICENSE.txt)
  [![Python](https://img.shields.io/badge/python-3.8+-blue)](https://python.org)
  [![PyQt6](https://img.shields.io/badge/GUI-PyQt6-green)](https://www.riverbankcomputing.com/software/pyqt/)
</div>

## � **Attribution & Credits**

> **🤝 Repository Origin**: This repository was originally taken from my colleague **BlackTechX** ([HacxGPT](https://github.com/BlackTechX011/Hacx-GPT)) and then enhanced with a complete desktop GUI interface, themes, and additional hacker tools.
> 
> **👥 Development**: The original CLI foundation by BlackTechX, desktop enhancement and GUI development by **TechnikGolem** with community contributions.
> 
> **📄 License**: Maintained under the same CC BY-NC-SA 4.0 license with proper attribution to original creator.

## �🚀 Features

### 🎨 **Multi-Theme Desktop GUI**
- **4 Stunning Themes**: Cyberpunk, Matrix Hacker, Gaming RGB, Modern Clean
- **Responsive Design** with PyQt6
- **Customizable Interface** (fonts, transparency, animations)

### 🤖 **Multiple AI Providers**
- **🆓 Free Providers**: Groq, Together AI, Replicate
- **Premium Providers**: OpenRouter, DeepSeek, Anthropic (Claude)
- **Smart Error Handling** with helpful suggestions
- **Easy Provider Switching**

### 💀 **Built-in Hacker Tools**
- **🎯 Port Scanner** - Scan network ports like Nmap
- **🔒 Hash Generator** - MD5, SHA1, SHA256, SHA512
- **📦 Base64 En/Decoder** - Data manipulation tools
- **🌐 Network Info** - DNS lookup, IP information

### ⚡ **Professional Features**
- **Streaming Chat** with real-time responses
- **Chat History** management
- **Markdown Rendering** for AI responses
- **Standalone .exe** builds (no Python required)
- **Cross-platform** compatibility

## 📦 Downloads

### 🔥 Ready-to-Use Executables

| Version | Size | Features | Download |
|---------|------|----------|----------|
| **HacxGPT_Fixed.exe** | 46MB | ✅ Best version with fixed APIs | [Download](releases/latest) |
| HacxGPT_Free.exe | 46MB | 🆓 Focus on free providers | [Download](releases/latest) |
| HacxGPT.exe | 46MB | 📦 Original version | [Download](releases/latest) |

**Recommended**: Use `HacxGPT_Fixed.exe` for the best experience!

## 🚀 Quick Start

### Option 1: Use Pre-built Executable (Easiest)
1. Download `HacxGPT_Fixed.exe` from [Releases](releases/latest)
2. Run the executable
3. Click "🆓 Kostenlose APIs" for free provider setup
4. Get a Groq API key from [console.groq.com](https://console.groq.com/keys)
5. Configure in Settings → Provider: "groq"
6. Start chatting!

### Option 2: Run from Source
```bash
# Clone repository
git clone https://github.com/BlackTechX011/HacxGPT-Desktop.git
cd HacxGPT-Desktop

# Install dependencies
pip install -r requirements.txt

# Run GUI version
python HacxGPT_GUI.py

# Or run CLI version
python HacxGPT.py
```

## 🆓 Free AI Providers Setup

### 🥇 Groq (Recommended)
- **Limit**: 14,400 requests/day
- **Speed**: Ultra-fast (hardware accelerated)
- **Models**: Llama 3.1 70B, Mixtral
- **Setup**: [console.groq.com](https://console.groq.com/keys)

### 🥈 Together AI
- **Credits**: $25 free credits
- **Models**: Llama 3, Mixtral, Qwen
- **Setup**: [api.together.xyz](https://api.together.xyz/)

### 🥉 Replicate
- **Credits**: $10 free credits
- **Models**: Llama 2/3, Code Llama
- **Setup**: [replicate.com](https://replicate.com/account/api-tokens)

## 🛠️ Build Your Own Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build standalone executable
pyinstaller --onefile --windowed --name "HacxGPT" HacxGPT_GUI.py

# Find your .exe in dist/ folder
```

## 🎨 Themes Preview

| Theme | Style | Colors |
|-------|-------|--------|
| **Cyberpunk** | Futuristic neon | Green/Pink on black |
| **Matrix Hacker** | Classic terminal | Green on black |
| **Gaming RGB** | Modern gaming | RGB colors |
| **Modern Clean** | Professional | Blue/white |

## 📱 Screenshots

*Coming soon - Upload your screenshots!*

## 🔧 Configuration

### Supported Providers
```json
{
  "groq": "Free 14.4k requests/day",
  "together": "$25 free credits", 
  "replicate": "$10 free credits",
  "openrouter": "Freemium model",
  "deepseek": "Free tier available",
  "anthropic": "Claude (paid)"
}
```

### Theme Customization
- Font size: 8-24px
- Transparency: 50-100%
- Animations: On/Off
- Sound effects: On/Off

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- Your OS and Python version
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**.

- ✅ **Share** - copy and redistribute
- ✅ **Adapt** - remix, transform, build upon
- ❌ **Commercial use** - not permitted
- 📝 **Attribution** - must give credit

See [LICENSE.txt](LICENSE.txt) for full details.

## 🙏 Credits

### Original Creator
- **BlackTechX** - Original HacxGPT concept and CLI version
- **GitHub**: [@BlackTechX011](https://github.com/BlackTechX011)
- **YouTube**: [@BlackTechX_](https://youtube.com/@BlackTechX_)

### Desktop GUI Enhancement
- **Enhanced by**: AI Assistant (Claude)
- **Features Added**: Desktop GUI, Hacker Tools, Multi-themes, Free providers
- **Repository Maintainer**: [Your GitHub Username]

### Technologies Used
- **PyQt6** - Desktop GUI framework
- **OpenAI SDK** - API client
- **PyInstaller** - Executable builder
- **Rich** - Terminal formatting (CLI version)

## � **Credits & Attribution**

### 👨‍💻 **Original Creator**
- **BlackTechX** - Original HacxGPT CLI project creator
- **Repository**: [github.com/BlackTechX011/Hacx-GPT](https://github.com/BlackTechX011/Hacx-GPT)
- **Social**: [@BlackTechX011](https://github.com/BlackTechX011)

### 🤝 **Repository Development**
- **Source**: This repository was taken from my colleague BlackTechX's original HacxGPT project
- **Enhancement**: Desktop GUI, themes, and hacker tools added by TechnikGolem
- **Collaboration**: Built upon BlackTechX's solid foundation with proper attribution

### 📜 **License Compliance**
- **Original License**: CC BY-NC-SA 4.0 (maintained)
- **Attribution**: Full credit to BlackTechX for the core concept and CLI implementation
- **Enhancements**: Desktop interface and additional features under same license

### 🌟 **Community**
- **Contributors**: Welcome community contributions
- **Inspiration**: BlackTechX's vision for accessible AI tools
- **Respect**: Maintaining the spirit of the original project

## �🔗 Links

- **🏠 Original Project**: [HacxGPT CLI](https://github.com/BlackTechX011/Hacx-GPT)
- **📱 Telegram**: [t.me/HacxGPT](https://t.me/HacxGPT)
- **📚 Documentation**: [Wiki](wiki)
- **🐛 Issues**: [GitHub Issues](issues)
- **💬 Discussions**: [GitHub Discussions](discussions)

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=TechnikGolem/HacxGPT-Desktop&type=Date)](https://star-history.com/#TechnikGolem/HacxGPT-Desktop&Date)

---

<div align="center">
  <b>🔥 Enhanced from BlackTechX's HacxGPT with desktop GUI and themes 🔥</b><br>
  <sub>Original concept by BlackTechX • Desktop enhancement by TechnikGolem</sub><br>
  <sub>If this project helped you, consider giving it a ⭐!</sub>
</div>