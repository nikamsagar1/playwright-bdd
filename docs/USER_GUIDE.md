# Playwright BDD Framework - User Guide

Welcome! This guide explains how to use the framework to write and run automated tests.

---

## Table of Contents
1. [Framework Overview](#framework-overview)
2. [Project Structure](#project-structure)
3. [Class Explanations](#class-explanations)
4. [How to Write Feature Files](#how-to-write-feature-files)
5. [How to Write Step Definitions](#how-to-write-step-definitions)
6. [How to Write Page Classes](#how-to-write-page-classes)
7. [How to Define Locators](#how-to-define-locators)
8. [How to Run Tests](#how-to-run-tests)
9. [Tips and Best Practices](#tips-and-best-practices)

---

## Framework Overview

This is a **Playwright BDD (Behavior-Driven Development)** automation framework. It allows you to:
- Write tests in plain English using Gherkin language
- Organize tests into feature files and step definitions
- Manage browser interactions through page objects
- Support multiple environments (QA, UAT, Production)
- Generate HTML reports

### Key Technologies
- **Playwright**: Browser automation library
- **pytest-bdd**: Makes BDD work with pytest
- **Python**: Programming language
- **Gherkin**: Plain English test syntax

---

## Project Structure

```
playwright-bdd/
├── config/                           # Configuration files
│   ├── env_config.json              # Environment URLs and credentials
│   └── execution_config.json        # Browser and execution settings
├── core/                             # Core framework classes
│   ├── config_reader.py             # Reads configuration files
│   ├── browser_manager.py           # Manages browser lifecycle
│   ├── page_factory.py              # Creates page objects
│   ├── app_context.py               # Application context (main entry point)
│   └── __init__.py
├── pages/                            # Page object classes
│   ├── login_page.py                # Login page interactions
│   ├── dashboard_page.py            # Dashboard page interactions
│   └── __init__.py
├── features/                         # Feature files (Gherkin)
│   ├── login.feature
│   └── add_user.feature
├── step_definitions/                 # Step definitions (Python code)
│   ├── login_steps.py
│   ├── test_add_user_steps.py
│   └── __init__.py
├── tests/                            # Test runner
│   ├── test_runner.py               # Main test entry point
│   └── __init__.py
├── screenshots/                      # Failed test screenshots
├── reports/                          # HTML test reports
├── conftest.py                       # Pytest configuration
├── pytest.ini                        # Pytest settings
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation
```

---

## Class Explanations

### 1. **ConfigReader** (`core/config_reader.py`)
**What it does**: Reads settings from JSON configuration files

**Purpose**:
- Loads environment settings (URLs, usernames, passwords)
- Loads browser settings (browser type, headless mode, timeouts)
- Provides configuration to other classes

**Example**:
```python
# Get environment configuration
env_config = ConfigReader.get_env_config()
base_url = env_config["environments"]["qa"]["base_url"]

# Get execution configuration  
exec_config = ConfigReader.get_execution_config()
browser_type = exec_config["browser"]
```

---

### 2. **BrowserManager** (`core/browser_manager.py`)
**What it does**: Opens and closes the browser

**Purpose**:
- Launches Playwright browser (Chrome, Firefox, Safari)
- Creates a page/tab
- Navigates to the base URL
- Closes browser after tests
- Handles browser settings (headless, viewport size, timeouts)

**Example**:
```python
manager = BrowserManager(execution_config)
browser, page = manager.launch_browser(base_url="https://example.com")
# ... run tests ...
manager.close_browser(browser)
```

---

### 3. **PageFactory** (`core/page_factory.py`)
**What it does**: Creates page objects (one per page)

**Purpose**:
- Creates page objects when needed
- Caches page objects so they're reused (same object for entire test)
- Ensures only one instance of each page exists

**Example**:
```python
factory = PageFactory(page)
login_page = factory.get_page(LoginPage)  # Created once
dashboard = factory.get_page(DashboardPage)  # Reused if called again
```

---

### 4. **AppContext** (`core/app_context.py`)
**What it does**: Main coordinator that manages everything

**Purpose**:
- Loads configurations
- Launches browser
- Creates PageFactory
- Provides page objects to tests
- Closes browser and takes screenshots on failure

**Example**:
```python
context = AppContext(env="qa")
context.setup("https://example.com")
login_page = context.get_page(LoginPage)
# ... run test ...
context.teardown()
```

---

### 5. **Page Classes** (`pages/login_page.py`, etc.)
**What it does**: Represents a single web page

**Purpose**:
- Contains locators (element selectors) for that page
- Contains methods to interact with that page
- Hides complexity of Playwright from step definitions

**Example**:
```python
class LoginPage:
    def __init__(self, page):
        self.page = page
    
    def enter_username(self, username):
        self.page.fill("input[name='username']", username)
    
    def click_login(self):
        self.page.click("button:has-text('Login')")
```

---

### 6. **Step Definitions** (`step_definitions/login_steps.py`, etc.)
**What it does**: Connects Gherkin text to Python code

**Purpose**:
- Reads the "Given/When/Then" steps from feature files
- Executes Python code for each step
- Uses page objects to interact with the application

**Example**:
```python
from pytest_bdd import given, when, then

@when("user enters valid username and password")
def enter_credentials(login_page):
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
```

---

## How to Write Feature Files

Feature files use **Gherkin language** - plain English that describes test scenarios.

### Location
`features/` folder (e.g., `features/login.feature`)

### Basic Structure

```gherkin
Feature: User Login

  Scenario: Admin can login with valid credentials
    Given user is on the login page
    When user enters valid username and password
    And user clicks on login button
    Then user should be logged in successfully

  Scenario: User cannot login with invalid credentials
    Given user is on the login page
    When user enters invalid username and password
    And user clicks on login button
    Then error message should be displayed
```

### Gherkin Keywords

| Keyword | Meaning | Example |
|---------|---------|---------|
| `Feature:` | Group of related tests | `Feature: User Management` |
| `Scenario:` | Single test case | `Scenario: Add new user` |
| `Given` | Starting condition | `Given user is logged in` |
| `When` | Action taken | `When user clicks submit` |
| `Then` | Expected result | `Then page shows success` |
| `And` | Multiple steps of same type | `And user enters password` |

### Tips
- Use simple, clear language
- Avoid technical jargon
- Use consistent wording (if you write "click login button" once, use it everywhere)
- One feature file per feature
- 3-5 scenarios per feature file is ideal

---

## How to Write Step Definitions

Step definitions connect your Gherkin text to Python code.

### Location
`step_definitions/` folder (e.g., `step_definitions/login_steps.py`)

### File Structure

```python
from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# ===== GIVEN STEPS (Setup/Preconditions) =====
@given("user is on the login page")
def user_on_login_page(app_context):
    """User should be on the login page"""
    login_page = app_context.get_page(LoginPage)
    # Page is already loaded by AppContext.setup()
    return login_page


# ===== WHEN STEPS (Actions) =====
@when("user enters valid username and password")
def enter_credentials(app_context):
    """Enter username and password"""
    login_page = app_context.get_page(LoginPage)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")


@when("user clicks on login button")
def click_login_button(app_context):
    """Click the login button"""
    login_page = app_context.get_page(LoginPage)
    login_page.click_login()


# ===== THEN STEPS (Assertions/Verification) =====
@then("user should be logged in successfully")
def verify_login(app_context):
    """Verify user is logged in"""
    dashboard = app_context.get_page(DashboardPage)
    assert dashboard.is_user_logged_in(), "User login failed"
```

### Best Practices

1. **Use descriptive names**: Make it clear what the step does
2. **One action per step**: Don't combine multiple actions
3. **Reuse steps**: Same step used in multiple scenarios
4. **Use app_context**: Gets page objects from AppContext
5. **Add docstrings**: Explain what the step does

### Common Patterns

```python
# Pattern 1: Getting a page object
login_page = app_context.get_page(LoginPage)

# Pattern 2: Doing multiple actions
@when("user completes login process")
def complete_login(app_context):
    login_page = app_context.get_page(LoginPage)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

# Pattern 3: Asserting/Verifying
@then("success message is displayed")
def verify_success(app_context):
    dashboard = app_context.get_page(DashboardPage)
    assert dashboard.get_success_message() is not None, "Success message not found"
```

---

## How to Write Page Classes

Page classes represent a single web page and contain all interactions for that page.

### Location
`pages/` folder (e.g., `pages/login_page.py`)

### File Structure

```python
class LoginPage:
    """Represents the Login page"""
    
    def __init__(self, page):
        """Initialize with Playwright page object"""
        self.page = page
        # Define locators in __init__
        self.username_field = "input[name='username']"
        self.password_field = "input[name='password']"
        self.login_button = "button:has-text('Login')"
        self.error_message = ".error-message"
    
    # ===== ACTIONS (Methods that DO something) =====
    def enter_username(self, username):
        """Enter username into the username field"""
        self.page.fill(self.username_field, username)
    
    def enter_password(self, password):
        """Enter password into the password field"""
        self.page.fill(self.password_field, password)
    
    def click_login(self):
        """Click the login button"""
        self.page.click(self.login_button)
    
    def open(self, base_url):
        """Open the login page"""
        self.page.goto(base_url)
    
    # ===== ASSERTIONS (Methods that CHECK something) =====
    def is_login_successful(self):
        """Check if login was successful"""
        # This should return True/False
        # You might check if we're on dashboard page
        return "dashboard" in self.page.url
    
    def get_error_message(self):
        """Get error message text"""
        try:
            return self.page.text_content(self.error_message)
        except:
            return None
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        try:
            self.page.wait_for_selector(self.error_message, timeout=5000)
            return True
        except:
            return False
```

### Method Types

| Type | Purpose | Example |
|------|---------|---------|
| **Action** | Do something on page | `click_login()`, `enter_username()` |
| **Navigation** | Go to a page | `open()`, `go_to_dashboard()` |
| **Assertion** | Check something | `is_login_successful()`, `is_error_shown()` |
| **Data Getter** | Get information | `get_error_message()`, `get_username()` |

### Tips
- Keep methods simple and focused
- One responsibility per method
- Use clear method names
- Add docstrings
- Return boolean for is_* methods
- Raise exceptions for failures (Playwright handles this)

---

## How to Define Locators

Locators are ways to find elements on a web page. They're usually stored at the top of page classes.

### Common Locator Types

```python
class LoginPage:
    def __init__(self, page):
        self.page = page
        
        # 1. CSS Selectors (most common)
        self.username_field = "input[name='username']"
        self.login_button = "button.btn-login"
        self.error_message = ".alert-error"
        
        # 2. XPath
        self.logout_button = "//button[contains(text(), 'Logout')]"
        
        # 3. Text matching
        self.submit_button = "button:has-text('Submit')"
        
        # 4. ID selector
        self.email_field = "#email"
        
        # 5. Class selector
        self.form_container = ".login-form"
        
        # 6. By placeholder
        self.search_box = "input[placeholder='Search...']"
        
        # 7. By role (recommended for accessibility)
        self.dialog = "role=dialog"
        self.button = "role=button"
```

### Tips for Finding Locators

1. **Use Browser DevTools**:
   - Right-click on element → Inspect
   - Copy the selector

2. **Prefer these (in order)**:
   - `id` (most stable)
   - `role` (good for accessibility)
   - Unique `class` or `name`
   - CSS selectors
   - XPath (last resort - slower)

3. **Bad locators** (will break easily):
   - Using position (`:nth-child(3)`)
   - Hardcoded text
   - Complex XPath

4. **Good locators** (stable):
   - Using unique attributes
   - Using semantic HTML (role, aria-label)
   - Short and simple CSS

### Using Locators in Methods

```python
def enter_username(self, username):
    """Enter username"""
    self.page.fill(self.username_field, username)

def click_login(self):
    """Click login button"""
    self.page.click(self.login_button)

def wait_for_error(self):
    """Wait for error to appear"""
    self.page.wait_for_selector(self.error_message, timeout=5000)
```

---

## How to Run Tests

### Prerequisites
```bash
# Install Python 3.10+
# Navigate to project folder
cd C:\PythonWorkspace\playwright-bdd

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Running Tests

#### 1. Run All Tests
```bash
pytest tests/test_runner.py -v
```

#### 2. Run Specific Environment
```bash
pytest tests/test_runner.py --env=qa -v
pytest tests/test_runner.py --env=uat -v
```

#### 3. Run in Headed Mode (See Browser)
```bash
pytest tests/test_runner.py --headed
```

#### 4. Run with HTML Report
```bash
pytest tests/test_runner.py --html=reports/report.html
```

#### 5. Run Specific Feature File
```bash
pytest tests/test_runner.py -k "Login" -v
```

#### 6. Stop on First Failure
```bash
pytest tests/test_runner.py -x
```

#### 7. Run with Full Output
```bash
pytest tests/test_runner.py -v -s
```

### Command Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-v` | Verbose output | `pytest tests/test_runner.py -v` |
| `-s` | Show print statements | `pytest tests/test_runner.py -s` |
| `-k` | Run by keyword | `pytest -k "login" tests/test_runner.py` |
| `-x` | Stop on first failure | `pytest tests/test_runner.py -x` |
| `--headed` | Show browser | `pytest tests/test_runner.py --headed` |
| `--env` | Select environment | `pytest tests/test_runner.py --env=qa` |

### View Reports
```bash
# Open HTML report
start reports/report.html

# View screenshots of failures
explorer screenshots/
```

---

## Tips and Best Practices

### 1. Naming Conventions
```python
# ❌ Bad
def test_login():
    pass

# ✅ Good
@when("user enters valid credentials")
def enter_valid_credentials(app_context):
    pass
```

### 2. Keep Steps Independent
```python
# ❌ Bad - Step depends on previous step
@when("user enters password")
def enter_password(login_page):
    # Assumes username was already entered
    login_page.enter_password("admin123")

# ✅ Good - Each step is complete
@when("user enters valid username and password")
def enter_credentials(app_context):
    login_page = app_context.get_page(LoginPage)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
```

### 3. Use Page Objects, Not Direct Playwright
```python
# ❌ Bad - Playwright code in step definition
@when("user logs in")
def user_logs_in(page):
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button:has-text('Login')")

# ✅ Good - Use page object
@when("user logs in")
def user_logs_in(app_context):
    login_page = app_context.get_page(LoginPage)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
```

### 4. Use Meaningful Assertions
```python
# ❌ Bad
assert True

# ✅ Good
assert dashboard.is_user_logged_in(), "User should be logged in after login"
```

### 5. Handle Waits Properly
```python
# ✅ Good - Playwright waits automatically
def click_login(self):
    self.page.click(self.login_button)

# ✅ Good - Explicit wait when needed
def wait_for_dashboard(self):
    self.page.wait_for_url("**/dashboard", timeout=10000)
```

### 6. Use Environment Configurations
```python
# ✅ Good - Don't hardcode URLs
# Use from config instead
env_config = ConfigReader.get_env_config()
base_url = env_config["environments"]["qa"]["base_url"]
```

### 7. Clean Code in Page Objects
```python
# ✅ Keep locators organized
class LoginPage:
    def __init__(self, page):
        # Group by section
        self.username_field = "input[name='username']"
        self.password_field = "input[name='password']"
        self.login_button = "button:has-text('Login')"
        
        # Another section
        self.error_message = ".alert-error"
        self.forgot_password = "a:has-text('Forgot Password')"
```

---

## Troubleshooting

### Test Fails: "Element not found"
```
Solution:
1. Check locator is correct (use DevTools)
2. Add wait before clicking
3. Check if page loaded completely
```

### Test Times Out
```
Solution:
1. Increase timeout: self.page.wait_for_selector(selector, timeout=15000)
2. Check if element actually exists
3. Check internet connection
```

### Browser Won't Open
```
Solution:
1. Run: playwright install
2. Check execution_config.json
3. Make sure browser type is correct
```

### Step Definition Not Found
```
Solution:
1. Check spelling matches exactly
2. Make sure file is in step_definitions/
3. Check import in conftest.py
```

---

## Next Steps

1. **Add your first feature file** in `features/`
2. **Write step definitions** in `step_definitions/`
3. **Create page classes** in `pages/`
4. **Run tests** with pytest
5. **Check reports** in `reports/`

---

## Need Help?

Refer to:
- [Playwright Documentation](https://playwright.dev/python/)
- [pytest-bdd Documentation](https://pytest-bdd.readthedocs.io/)
- [Gherkin Syntax Guide](https://cucumber.io/docs/gherkin/)

Happy testing! 🚀
