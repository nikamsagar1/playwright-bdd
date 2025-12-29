# Framework Architecture & Best Practices

## How the Framework Works - Step by Step

### Test Execution Flow

```
1. User runs: pytest tests/test_runner.py --env=qa --headed
                          ↓
2. pytest finds conftest.py and loads fixtures
                          ↓
3. conftest.py creates AppContext fixture
                          ↓
4. AppContext loads configuration (env_config.json, execution_config.json)
                          ↓
5. BrowserManager launches browser
                          ↓
6. pytest-bdd loads feature files from features/
                          ↓
7. For each scenario in feature file:
   - Find matching step definitions in step_definitions/
   - Execute each step
   - Get page objects from PageFactory
   - Use page objects to interact with app
   - Capture screenshots if failed
                          ↓
8. Generate HTML report
                          ↓
9. Cleanup: Close browser
```

### Class Interaction Diagram

```
conftest.py (Pytest Config)
    ↓
AppContext (Main Coordinator)
    ├── ConfigReader (Load settings)
    ├── BrowserManager (Open browser)
    └── PageFactory (Create page objects)
            ↓
        Page Objects (LoginPage, DashboardPage, etc.)
            ├── Locators (CSS, XPath selectors)
            └── Methods (enter_username, click_login, etc.)
            ↓
Step Definitions (login_steps.py, etc.)
    ↓
Feature Files (login.feature, etc.)
```

---

## Configuration Management

### Understanding env_config.json

```json
{
  "environments": {
    "qa": {
      "base_url": "https://qa.example.com",
      "credentials": {
        "username": "admin",
        "password": "pass123"
      },
      "timeouts": {
        "page_load": 30000,
        "element": 10000
      }
    },
    "uat": {
      "base_url": "https://uat.example.com",
      ...
    },
    "prod": {
      "base_url": "https://example.com",
      ...
    }
  },
  "default_env": "qa"
}
```

**Why different environments?**
- QA: Testing environment (safe to break)
- UAT: User acceptance testing (client approves)
- PROD: Production (real users)

### Understanding execution_config.json

```json
{
  "browser": "chromium",           # Browser type
  "headless": true,                # Hide browser window
  "viewport": {"width": 1920, "height": 1080},  # Screen size
  "timeout": 30000,                # Wait timeout (ms)
  "trace": "on-first-retry",       # Debug trace
  "video": "retain-on-failure"     # Video recording
}
```

---

## Design Patterns Used

### 1. Page Object Model (POM)

**What is it?**
Represents each web page as a Python class with:
- Locators (element selectors)
- Methods (actions and assertions)

**Why use it?**
- Reduces code duplication
- Easy to maintain (change selector in one place)
- Separates page logic from test logic

**Example**:
```python
# Page Object (pages/login_page.py)
class LoginPage:
    def enter_username(self, username):
        self.page.fill(self.username_field, username)

# Step Definition (step_definitions/login_steps.py)
@when("user enters username")
def enter_username(app_context):
    login_page = app_context.get_page(LoginPage)
    login_page.enter_username("admin")

# Benefit: If username field selector changes, update only in LoginPage
```

### 2. Fixture Pattern

**What is it?**
Reusable setup/teardown code using pytest fixtures

**Why use it?**
- Automatic browser launch/close
- Automatic configuration loading
- Run before each test, clean up after

**Example**:
```python
@pytest.fixture(scope="function")
def app_context(request):
    context = AppContext()
    context.setup()
    yield context  # Test runs here
    context.teardown()  # Cleanup
```

### 3. Factory Pattern

**What is it?**
Creates objects on demand

**Why use it?**
- Only create what you need
- Cache objects (don't recreate)

**Example**:
```python
class PageFactory:
    def get_page(self, page_class):
        if page_class not in self.pages:
            self.pages[page_class] = page_class(self.page)
        return self.pages[page_class]  # Reuse if exists
```

### 4. Singleton Pattern (Page Objects)

**What is it?**
Only one instance of each page per test

**Why use it?**
- Consistent state
- Better performance
- Easier debugging

**How**:
PageFactory ensures only one LoginPage, one DashboardPage, etc.

---

## Best Practices by Category

### Feature Files

```gherkin
# ✅ GOOD: Clear, readable, independent
Feature: User Login
  
  Scenario: Admin can login with valid credentials
    Given user is on login page
    When user enters "admin" as username
    And user enters "password123" as password
    And user clicks login button
    Then dashboard is displayed
    And welcome message shows "Welcome, admin"

# ❌ BAD: Vague, dependent, too many steps
Feature: Login and stuff
  
  Scenario: Test login
    When user does login
    Then page works
```

### Step Definitions

```python
# ✅ GOOD: Simple, readable, one action
@when("user enters valid credentials")
def enter_credentials(app_context):
    login_page = app_context.get_page(LoginPage)
    login_page.enter_username("admin")
    login_page.enter_password("pass123")

# ❌ BAD: Too complex, multiple scenarios
@when("user does login with different scenarios")
def login_scenarios(app_context, scenario):
    if scenario == "valid":
        # ... code
    elif scenario == "invalid":
        # ... code
```

### Page Objects

```python
# ✅ GOOD: Clear methods, good organization
class LoginPage:
    def __init__(self, page):
        self.username_field = "input[name='username']"
        self.password_field = "input[name='password']"
        self.login_button = "button:has-text('Login')"
    
    def enter_username(self, username):
        """Enter username"""
        self.page.fill(self.username_field, username)
    
    def enter_password(self, password):
        """Enter password"""
        self.page.fill(self.password_field, password)

# ❌ BAD: Messy, duplicate code
class LoginPage:
    def do_something(self, data):
        self.page.fill("input[name='username']", data)
        self.page.fill("input[name='password']", data)
        # ... more code ...
```

### Locators

```python
# ✅ GOOD: Stable, semantic
self.username = "input[name='username']"
self.login_button = "button[type='submit']"
self.error_message = "[role='alert']"

# ❌ BAD: Fragile, brittle
self.username = "//*[@class='form']/input[1]"  # Position-based
self.button = "//button[contains(text(), 'Log')]"  # Text-based
```

---

## Testing Strategies

### 1. Smoke Testing (Quick Check)
```bash
# Run critical tests only
pytest tests/test_runner.py -k "smoke" --env=qa
```

### 2. Regression Testing (Full Coverage)
```bash
# Run all tests
pytest tests/test_runner.py --env=qa
```

### 3. Sanity Testing (Before Release)
```bash
# Run important scenarios
pytest tests/test_runner.py -k "sanity" --env=uat
```

### 4. Parallel Testing (Speed Up)
```bash
# Install pytest-xdist
pip install pytest-xdist

# Run in parallel
pytest tests/test_runner.py -n auto
```

---

## Common Mistakes & Solutions

### Mistake 1: Hardcoding URLs
```python
# ❌ BAD
def goto_login(self):
    self.page.goto("https://example.com/login")

# ✅ GOOD
def goto_login(self, base_url):
    self.page.goto(base_url)
```

### Mistake 2: Weak Locators
```python
# ❌ BAD - Will break if text changes
self.submit_button = "//button[text()='Submit']"

# ✅ GOOD - Stable
self.submit_button = "button[type='submit']"
```

### Mistake 3: No Waits
```python
# ❌ BAD - Element might not exist yet
self.page.click(self.button)

# ✅ GOOD - Wait for element
self.page.wait_for_selector(self.button, timeout=5000)
self.page.click(self.button)
```

### Mistake 4: Creating New Objects
```python
# ❌ BAD - Creates new object each time
@when("user clicks login")
def click_login(page):
    login_page = LoginPage(page)  # NEW OBJECT
    login_page.click_login()

# ✅ GOOD - Reuse via PageFactory
@when("user clicks login")
def click_login(app_context):
    login_page = app_context.get_page(LoginPage)  # SAME OBJECT
    login_page.click_login()
```

### Mistake 5: No Error Handling
```python
# ❌ BAD - Fails without explanation
assert login_page.is_logged_in()

# ✅ GOOD - Clear error message
assert login_page.is_logged_in(), "Login failed - dashboard not shown"
```

---

## Performance Tips

### 1. Use Headless Mode for CI/CD
```bash
# Faster - no UI rendering
pytest tests/test_runner.py --env=qa

# Slower - renders UI
pytest tests/test_runner.py --env=qa --headed
```

### 2. Increase Timeouts for Slow Apps
```json
{
  "timeout": 30000,  // Increase to 60000
  "page_load": 60000
}
```

### 3. Run Tests in Parallel
```bash
pip install pytest-xdist
pytest tests/test_runner.py -n auto
```

### 4. Use Appropriate Waits
```python
# ❌ BAD - Always wait 5 seconds
time.sleep(5)

# ✅ GOOD - Wait until element appears
self.page.wait_for_selector(self.element, timeout=10000)
```

### 5. Cache Dependencies in CI/CD
```yaml
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

---

## Debugging Tests

### 1. Run in Headed Mode
```bash
pytest tests/test_runner.py --headed -s
```

### 2. Use Print Statements
```python
@when("user clicks login")
def click_login(app_context):
    print("DEBUG: About to click login button")
    login_page = app_context.get_page(LoginPage)
    login_page.click_login()
    print("DEBUG: Login button clicked")
```

### 3. Check Screenshots
```bash
# Failed test screenshots are in:
screenshots/test_admin_can_add_a_new_user_20251229_154837.png
```

### 4. Enable Traces (Advanced)
```json
{
  "trace": "on-first-retry"  // Record trace on failure
}
```

### 5. Use Debugger
```python
@when("user clicks login")
def click_login(app_context):
    import pdb; pdb.set_trace()  # Pause here
    login_page = app_context.get_page(LoginPage)
```

---

## Scaling the Framework

### Adding New Feature
1. Create `features/new_feature.feature`
2. Create step definitions file
3. Create page object classes
4. Import in test_runner.py
5. Run tests

### Adding New Environment
1. Add to `env_config.json`:
   ```json
   "prod": {
     "base_url": "https://prod.example.com",
     ...
   }
   ```
2. Run with: `pytest tests/test_runner.py --env=prod`

### Integrating with CI/CD
1. Copy `azure-pipelines.yml` or `.github/workflows/run-tests.yml`
2. Update repo settings
3. Push code
4. Tests run automatically!

---

## Framework Strengths

✅ **Easy to Learn**: Plain English scenarios  
✅ **Maintainable**: Page objects organize code  
✅ **Flexible**: Works with any web app  
✅ **Fast**: Parallel test execution  
✅ **Reliable**: Stable locators and waits  
✅ **Scalable**: Grow with your project  

---

## Summary

This framework combines:
- **Gherkin** for readable tests
- **Pytest** for execution
- **Playwright** for automation
- **Page Objects** for organization
- **Configuration files** for flexibility

Result: Professional, maintainable test automation! 🚀

---

## Quick Reference

| Task | Command |
|------|---------|
| Run all tests | `pytest tests/test_runner.py -v` |
| Run on QA | `pytest tests/test_runner.py --env=qa` |
| See browser | `pytest tests/test_runner.py --headed` |
| Generate report | `pytest tests/test_runner.py --html=reports/report.html` |
| Stop on failure | `pytest tests/test_runner.py -x` |
| Specific test | `pytest tests/test_runner.py -k "login"` |

---

**Remember**: The framework is here to make your life easier, not harder. Keep it simple! 😊
