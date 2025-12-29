# Playwright BDD Automation Framework

Professional-grade test automation framework using Playwright and pytest-bdd.

## 📖 Documentation

All documentation is located in the **[docs/](docs/)** folder:

- **[START_HERE.md](docs/START_HERE.md)** - Quick overview and learning paths
- **[QUICKSTART.md](docs/QUICKSTART.md)** - 5-minute setup and first test
- **[USER_GUIDE.md](docs/USER_GUIDE.md)** - Complete manual with examples
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Technical deep dive
- **[CI_CD_GUIDE.md](docs/CI_CD_GUIDE.md)** - GitHub Actions & Azure DevOps setup
- **[QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md)** - Cheat sheet
- **[GLOSSARY.md](docs/GLOSSARY.md)** - Terms and definitions
- **[DOCUMENTATION_INDEX.md](docs/DOCUMENTATION_INDEX.md)** - Full navigation

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run tests
pytest tests/test_runner.py --env=qa --headed

# 3. View report
open reports/report.html
```

## 📁 Project Structure

```
├── config/                 # Configuration files (environments, settings)
├── core/                   # Framework core (ConfigReader, BrowserManager, etc.)
├── features/              # Gherkin feature files
├── pages/                 # Page Object Model (page classes)
├── step_definitions/      # BDD step implementations
├── tests/                 # Test runners
├── docs/                  # 📖 All documentation
├── YAML/                  # CI/CD workflows (GitHub Actions, Azure DevOps)
└── requirements.txt       # Python dependencies
```

## 🔧 CI/CD Workflows

CI/CD configuration files are in **[YAML/](YAML/)** folder:
- `run-tests.yml` - GitHub Actions workflow
- `azure-pipelines.yml` - Azure DevOps pipeline

## 📚 New to the Framework?

1. **Start here:** [START_HERE.md](docs/START_HERE.md)
2. **Quick setup:** [QUICKSTART.md](docs/QUICKSTART.md)
3. **Full guide:** [USER_GUIDE.md](docs/USER_GUIDE.md)

---

**Questions?** Check [GLOSSARY.md](docs/GLOSSARY.md) or [DOCUMENTATION_INDEX.md](docs/DOCUMENTATION_INDEX.md) for complete navigation.
