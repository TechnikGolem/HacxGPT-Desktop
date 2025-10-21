# Contributing to HacxGPT Desktop

First off, thank you for considering contributing to HacxGPT Desktop! 🎉

## 🤝 How to Contribute

### 🐛 Reporting Bugs

Before creating bug reports, please check if the issue already exists. When creating a bug report, include:

- **Clear description** of the problem
- **Steps to reproduce** the behavior
- **Expected behavior** vs what actually happened
- **Screenshots** if applicable
- **System information**:
  - OS (Windows/Linux/Mac)
  - Python version
  - PyQt6 version
  - HacxGPT version

### 💡 Suggesting Features

Feature requests are welcome! Please:

- **Check existing issues** to avoid duplicates
- **Provide clear description** of the feature
- **Explain why it would be useful**
- **Consider implementation complexity**

### 🔧 Code Contributions

#### Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/HacxGPT-Desktop.git
cd HacxGPT-Desktop

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

#### Development Guidelines

1. **Code Style**
   - Follow PEP 8 Python style guide
   - Use meaningful variable names
   - Add comments for complex logic
   - Keep functions small and focused

2. **PyQt6 Guidelines**
   - Use signal/slot connections properly
   - Handle UI updates in main thread
   - Implement proper error handling
   - Follow Qt naming conventions

3. **Testing**
   - Test on multiple providers
   - Verify UI responsiveness
   - Check theme compatibility
   - Test executable builds

#### Pull Request Process

1. **Fork** the repository
2. **Create branch** from main: `git checkout -b feature/awesome-feature`
3. **Make changes** following guidelines
4. **Test thoroughly** on your system
5. **Commit** with clear messages
6. **Push** to your fork
7. **Create Pull Request** with description

#### Commit Message Format

```
type(scope): brief description

- Detailed explanation if needed
- Multiple points allowed
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style/formatting
- `refactor`: Code refactoring
- `test`: Tests
- `build`: Build system

**Examples:**
```
feat(gui): add dark mode theme option
fix(api): handle groq rate limit errors
docs(readme): update installation instructions
```

## 🎨 Contributing Areas

### High Priority
- **🐛 Bug fixes** for existing features
- **🚀 Performance improvements**
- **📚 Documentation** enhancements
- **🧪 Testing** improvements

### Medium Priority
- **🎨 New themes** or theme improvements
- **🔧 New hacker tools**
- **🤖 Additional AI providers**
- **📱 UI/UX improvements**

### Low Priority
- **🌍 Internationalization** (translations)
- **📊 Analytics/logging** features
- **🔌 Plugin system**
- **📦 Package management**

## 🏗️ Architecture Overview

```
HacxGPT_GUI.py
├── Themes (color schemes)
├── Config (settings management)
├── HackerTools (security tools)
│   ├── PortScanner
│   ├── HashGenerator
│   ├── Base64Tools
│   └── NetworkInfo
├── LLMClient (AI provider interface)
├── UI Components
│   ├── MainWindow
│   ├── SettingsDialog
│   └── HackerToolsDialog
└── Utilities
```

## 📋 Development Tasks

### Easy (Good First Issues)
- [ ] Add new hash algorithms
- [ ] Improve error messages
- [ ] Add keyboard shortcuts
- [ ] Update documentation
- [ ] Fix UI layout issues

### Medium
- [ ] Add new themes
- [ ] Implement file drag-and-drop
- [ ] Add chat export functionality
- [ ] Improve port scanner performance
- [ ] Add more network tools

### Hard
- [ ] Voice chat integration
- [ ] Plugin architecture
- [ ] Multi-language support
- [ ] Advanced AI model selection
- [ ] Distributed chat (P2P)

## 🔍 Code Review Checklist

- [ ] Code follows style guidelines
- [ ] Changes are tested
- [ ] Documentation is updated
- [ ] No unnecessary dependencies
- [ ] Error handling is proper
- [ ] UI is responsive
- [ ] Themes work correctly
- [ ] API providers function
- [ ] Build process works

## 🎯 Focus Areas

1. **Stability** - Ensure robust error handling
2. **Performance** - Keep UI responsive
3. **Usability** - Intuitive interface design
4. **Security** - Safe API key handling
5. **Compatibility** - Cross-platform support

## 📞 Getting Help

- **Discord**: [Join our server](https://discord.gg/hacxgpt)
- **GitHub Issues**: For bugs and features
- **Discussions**: For questions and ideas
- **Email**: [maintainer@email.com]

## 🏆 Recognition

Contributors will be:
- Listed in README.md
- Mentioned in release notes
- Given appropriate GitHub roles
- Featured on project website

## 📜 License

By contributing, you agree that your contributions will be licensed under the same CC BY-NC-SA 4.0 license that covers the project.

---

**Thank you for making HacxGPT Desktop better! 🚀**