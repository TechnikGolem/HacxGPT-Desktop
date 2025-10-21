# Security Policy

## 🔒 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | ✅ Yes             |
| 1.x     | ❌ No (Legacy CLI) |

## 🚨 Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 🔐 Private Disclosure

**DO NOT** open a public GitHub issue for security vulnerabilities.

Instead, please:

1. **Email us privately**: security@hacxgpt.com
2. **Include details**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### 📧 Contact Methods

- **Primary**: security@hacxgpt.com
- **Backup**: [Create private issue on GitHub]
- **Telegram**: @HacxGPTSecurity (for urgent issues)

### ⏱️ Response Timeline

- **Initial response**: Within 48 hours
- **Assessment**: Within 7 days
- **Fix timeline**: Varies by severity
- **Public disclosure**: After fix is released

## 🛡️ Security Considerations

### API Key Security

- ✅ API keys are stored locally only
- ✅ Keys are not transmitted except to respective AI providers
- ✅ Environment files (.hacx) are in .gitignore
- ⚠️ Users should never share API keys publicly

### Network Security

- ✅ All API communications use HTTPS
- ✅ No telemetry or data collection
- ✅ Local execution only
- ⚠️ Port scanner respects network boundaries

### Code Security

- ✅ No arbitrary code execution
- ✅ Input validation on all user inputs
- ✅ Safe file handling practices
- ⚠️ Hacker tools are for educational purposes only

### Build Security

- ✅ PyInstaller builds are reproducible
- ✅ No backdoors or malicious code
- ✅ Source code is fully available
- ⚠️ Always download executables from official releases

## 🚫 Out of Scope

The following are **NOT** considered security vulnerabilities:

- Rate limiting by AI providers
- API costs incurred by users
- Network scanning detection by firewalls
- Educational hacking tool usage
- UI rendering issues
- Performance problems

## 🔍 Security Features

### Data Protection
- **No data collection**: Everything stays local
- **Encrypted storage**: API keys are safely stored
- **Memory safety**: Sensitive data cleared after use
- **Audit trail**: Local logs only (optional)

### Network Safety
- **Firewall friendly**: Respects network rules
- **Rate limiting**: Built-in request throttling
- **Error handling**: Graceful failure modes
- **Connection security**: SSL/TLS verification

### Code Safety
- **Input sanitization**: All user inputs validated
- **Dependency security**: Regular security updates
- **Code review**: All changes reviewed
- **Static analysis**: Automated security scanning

## ⚡ Incident Response

If a security issue is confirmed:

1. **Immediate action**: Disable affected features if needed
2. **Develop fix**: Create secure solution
3. **Testing**: Verify fix doesn't break functionality
4. **Release**: Push update as soon as possible
5. **Communication**: Notify users of security update
6. **Follow-up**: Monitor for related issues

## 📋 Security Checklist for Contributors

Before submitting code, ensure:

- [ ] No hardcoded credentials or secrets
- [ ] Input validation for all user data
- [ ] Error messages don't leak sensitive info
- [ ] Network calls use proper encryption
- [ ] File operations are sandboxed
- [ ] Dependencies are up-to-date
- [ ] Code follows security best practices

## 🏆 Security Hall of Fame

We recognize security researchers who help improve HacxGPT:

| Researcher | Vulnerability | Date | Severity |
|------------|---------------|------|----------|
| *None yet* | *Be the first!* | - | - |

## 📚 Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Guidelines](https://python-security.readthedocs.io/)
- [PyQt Security Best Practices](https://doc.qt.io/qt-6/security.html)
- [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist)

## 🔄 Updates

This security policy may be updated periodically. Check back for the latest version.

---

**Last updated**: October 21, 2025
**Version**: 1.0