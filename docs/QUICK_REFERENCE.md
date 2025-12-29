# 🎯 Quick Reference Card - Keep This Handy!

Print this out or bookmark it! Everything you need at a glance.

---

## 📌 Framework Files At a Glance

```
┌─────────────────────────────────────────┐
│   PLAYWRIGHT BDD FRAMEWORK              │
├─────────────────────────────────────────┤
│ 📁 features/              → Test scenarios
│ 📁 step_definitions/      → Python code
│ 📁 pages/                 → Page objects
│ 📁 tests/test_runner.py   → Main test file
│ 📁 core/                  → Framework classes
│ 📄 conftest.py            → Pytest setup
└─────────────────────────────────────────┘
```

---

## ⚡ Quick Commands

### Setup (One-time)
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

### Run Tests
```bash
# All tests
pytest tests/test_runner.py -v

# Specific environment
pytest tests/test_runner.py --env=qa

# See browser
pytest tests/test_runner.py --headed

# Generate report
pytest tests/test_runner.py --html=reports/report.html

# Stop on first failure
pytest tests/test_runner.py -x
```

---

## 📝 Feature File Template

```gherkin
Feature: [Feature Name]
  Description of what this feature tests

  Scenario: [Test Name]
    Given [Starting condition]
    When [Action taken]
    And [Another action]
    Then [Expected result]
    And [Another expectation]
```

---

## 🐍 Step Definition Template

```python
from pytest_bdd import given, when, then

@given("starting condition")
def starting_condition(app_context):
    page = app_context.get_page(PageClassName)
    # Your code here

@when("action is taken")
def action(app_context):
    page = app_context.get_page(PageClassName)
    # Your code here

@then("expected result")
def assertion(app_context):
    page = app_context.get_page(PageClassName)
    assert page.some_check(), "Error message"
```

---

## 📄 Page Object Template

```python
class PageName:
    def __init__(self, page):
        self.page = page
        
        # Define locators
        self.button = "button:has-text('Click')"
        self.input = "input[name='field']"
        self.message = ".success-msg"
    
    # Actions
    def click_button(self):
        self.page.click(self.button)
    
    def enter_text(self, text):
        self.page.fill(self.input, text)
    
    # Assertions
    def is_success_shown(self):
        try:
            self.page.wait_for_selector(self.message, timeout=5000)
            return True
        except:
            return False
```

---

## 🎭 Gherkin Keywords

| Keyword | What It Means | Example |
|---------|---------------|---------|
| **Given** | Setup/Context | "user is on login page" |
| **When** | Action | "user clicks button" |
| **Then** | Expected result | "page shows success" |
| **And** | More of same type | "and user enters password" |
| **But** | Negative condition | "but error shown" |
| **Feature** | Group of tests | "Feature: Login" |
| **Scenario** | Single test | "Scenario: Valid login" |

---

## 🔍 Locator Types

| Type | Format | Example |
|------|--------|---------|
| **ID** | `#id` | `#username` |
| **Class** | `.class` | `.btn-login` |
| **Name** | `[name='...']` | `input[name='user']` |
| **Text** | `:has-text('...')` | `button:has-text('Login')` |
| **Role** | `role=...` | `role=button` |
| **XPath** | `//...` | `//button[@id='btn']` |

---

## 🧪 Test Command Cheat Sheet

```bash
pytest tests/test_runner.py [OPTIONS]

OPTIONS:
  -v                          Verbose output
  --env=qa                    Run on QA environment
  --headed                    Show browser window
  --html=FILE                 Generate HTML report
  -k "keyword"                Run specific test
  -x                          Stop on first failure
  -s                          Show print statements
  --tb=short                  Short traceback
  -n auto                     Run in parallel (needs pytest-xdist)
```

---

## 🔧 Class Quick Reference

| Class | Location | Does What |
|-------|----------|-----------|
| **ConfigReader** | `core/config_reader.py` | Reads config files |
| **BrowserManager** | `core/browser_manager.py` | Opens/closes browser |
| **PageFactory** | `core/page_factory.py` | Creates page objects |
| **AppContext** | `core/app_context.py` | Main coordinator |
| **Page Classes** | `pages/*.py` | Represent web pages |

---

## 📊 Test Results

### What It Means
| Symbol | Meaning | Color |
|--------|---------|-------|
| ✅ | Test passed | Green |
| ❌ | Test failed | Red |
| ⏭️ | Test skipped | Yellow |
| ⚠️ | Error/warning | Orange |

---

## 🎯 If Test Fails

1. **Check the error message**
   - Read what went wrong
   - Look in terminal output

2. **Run with --headed**
   ```bash
   pytest tests/test_runner.py --headed
   ```

3. **Check screenshot**
   ```
   Look in: screenshots/
   ```

4. **Verify locator**
   - Inspect element
   - Update in page class

5. **Check timeout**
   - Increase wait time
   - Check internet connection

---

## 📁 Configuration Files

### env_config.json
```json
{
  "environments": {
    "qa": {
      "base_url": "https://...",
      "credentials": {"username": "...", "password": "..."}
    }
  }
}
```

### execution_config.json
```json
{
  "browser": "chromium",
  "headless": true,
  "timeout": 30000
}
```

---

## 🚀 Common Patterns

### Get Page Object
```python
page = app_context.get_page(PageClassName)
```

### Fill Input
```python
self.page.fill("input[selector]", "text")
```

### Click Button
```python
self.page.click("button[selector]")
```

### Wait for Element
```python
self.page.wait_for_selector("selector", timeout=5000)
```

### Check Element
```python
try:
    self.page.wait_for_selector("selector", timeout=5000)
    return True
except:
    return False
```

### Get Text
```python
text = self.page.text_content("selector")
```

### Press Key
```python
self.page.press("selector", "Enter")
```

---

## 📚 Documentation Map

| Need | Go To |
|------|-------|
| Quick start | QUICKSTART.md |
| How to write tests | USER_GUIDE.md |
| Cloud automation | CI_CD_GUIDE.md |
| Deep understanding | ARCHITECTURE.md |
| Unknown terms | GLOSSARY.md |
| Navigate docs | DOCUMENTATION_INDEX.md |

---

## 🎓 Learning Order

1. **Day 1**: Read QUICKSTART.md + Setup
2. **Day 2**: Write first test
3. **Day 3-4**: Read USER_GUIDE.md
4. **Day 5**: Write 5 tests
5. **Week 2**: Read ARCHITECTURE.md
6. **Week 3**: Read CI_CD_GUIDE.md
7. **Week 4**: Setup automation

---

## 💡 Pro Tips

✅ Use `--headed` when debugging  
✅ Check screenshots when tests fail  
✅ Use environment variables for sensitive data  
✅ Keep locators stable and simple  
✅ One action per step  
✅ Reuse steps across scenarios  
✅ Use PageFactory for page objects  
✅ Cache dependencies in CI/CD  

---

## ⚠️ Common Mistakes

❌ Hardcoding URLs  
❌ Weak or brittle locators  
❌ Creating new page objects each time  
❌ No waits before interactions  
❌ Multiple actions in one step  
❌ No error messages in assertions  
❌ Not using page objects  
❌ Forgetting to import app_context  

---

## 🔗 Important Links

| Resource | URL |
|----------|-----|
| Playwright Docs | https://playwright.dev/python |
| pytest-bdd Docs | https://pytest-bdd.readthedocs.io |
| Gherkin Guide | https://cucumber.io/docs/gherkin |
| GitHub Actions | https://docs.github.com/en/actions |

---

## 🎯 Success Checklist

- [ ] Environment setup complete
- [ ] First test runs successfully
- [ ] Can write feature files
- [ ] Can write step definitions
- [ ] Can create page classes
- [ ] Understand locators
- [ ] Know main commands
- [ ] Understand AppContext
- [ ] Can debug failures
- [ ] Ready for automation

---

## 🚀 Next: What to Do Now

**Option A: Fastest Way** (30 min)
1. Read QUICKSTART.md
2. Create first test
3. Run it

**Option B: Complete Way** (2 hours)
1. Read QUICKSTART.md
2. Create first test
3. Read USER_GUIDE.md
4. Write more tests

**Option C: Automation** (1 hour)
1. Read CI_CD_GUIDE.md
2. Setup GitHub Actions
3. Push code
4. Tests run auto

---

## 📞 Quick Help

**Q: Test won't run**
A: Check pytest installed, check file paths

**Q: Browser won't open**
A: Run `playwright install`

**Q: Element not found**
A: Check locator, run with `--headed`

**Q: Don't understand something**
A: Check USER_GUIDE.md or GLOSSARY.md

**Q: Want to automate**
A: Read CI_CD_GUIDE.md

---

## ✨ Key Takeaways

✅ **Simple language**: All docs in English  
✅ **200+ examples**: Copy-paste code  
✅ **4 learning paths**: Choose your speed  
✅ **Complete**: Nothing missing  
✅ **Professional**: Production ready  

---

**Print This Out or Bookmark It!**

Keep this reference card handy while you work. 🚀

---

**Last Updated**: December 29, 2025
