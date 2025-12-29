# 🎭 Playwright BDD Automation Framework - Complete Beginner's Guide

Welcome! This is a **professional-grade test automation framework** that anyone can learn and use, even with zero automation knowledge.

**What is this?** A tool to automatically test websites by simulating user actions (clicks, typing, form submissions, etc.) and verifying expected results.

---

## 📚 Table of Contents

1. [What You'll Learn](#what-youll-learn)
2. [Prerequisites (What You Need to Know)](#prerequisites)
3. [Complete Setup Guide](#complete-setup-guide)
4. [Project Structure Explained](#project-structure-explained)
5. [Configuration Setup](#configuration-setup)
6. [Your First Test](#your-first-test)
7. [Running Tests](#running-tests)
8. [Writing More Tests](#writing-more-tests)
9. [Common Issues & Solutions](#common-issues--solutions)
10. [Best Practices](#best-practices)
11. [Glossary](#glossary)

---

## 🎯 What You'll Learn

By using this framework, you'll learn:
- ✅ How to automate website testing
- ✅ How to write tests in human-readable language (Gherkin)
- ✅ How to organize test code professionally (Page Object Model)
- ✅ How to manage configurations for different environments
- ✅ How to run tests and generate reports

---

## 📋 Prerequisites (What You Need to Know)

**Don't worry if you don't know these yet** - we'll explain as we go!

### Software You Need Installed:
1. **Python 3.8+** - Programming language
   - Download: https://www.python.org/downloads/
   - ✅ **Important**: Check "Add Python to PATH" during installation

2. **VS Code** - Code editor
   - Download: https://code.visualstudio.com/

3. **Git** (optional) - For version control
   - Download: https://git-scm.com/

### Concepts You Should Know (Basic):
- **Python basics** - variables, functions, imports
- **JSON** - simple data format (don't worry, we provide examples)
- **Command line / Terminal** - running commands
- **Web browsers** - Chrome, Firefox, Edge

---

## 🚀 Complete Setup Guide

### Step 1: Verify Python Installation ✅

Open PowerShell (Windows) or Terminal (Mac/Linux):
```bash
python --version
```

You should see: `Python 3.8.x` or higher.

**If this fails:**
- Python might not be installed
- Or not added to PATH
- Reinstall Python and check "Add Python to PATH" ✓

---

### Step 2: Navigate to Project Folder

```bash
cd C:\PythonWorkspace\playwright-bdd
```

Replace with your actual project path if different.

---

### Step 3: Create Virtual Environment

A **virtual environment** is an isolated Python workspace where we install only the packages we need.

```bash
python -m venv venv
```

This creates a `venv/` folder.

---

### Step 4: Activate Virtual Environment

**Windows (PowerShell):**
```bash
& venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

✅ You'll see `(venv)` at the start of your terminal line when active.

---

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

This installs all required packages (pytest, playwright, etc.).

**Wait for it to complete** - it takes a minute or two.

---

### Step 6: Install Playwright Browsers

```bash
python -m playwright install
```

This downloads Chrome, Firefox, and other browsers that automation will use.

**This also takes a few minutes.**

---

### Step 7: Verify Installation

Run a quick test:
```bash
python -m pytest --version
```

You should see: `pytest 9.0.x` or similar.

✅ **Installation Complete!**

---

## 📁 Project Structure Explained

```
playwright-bdd/
│
├── 📁 config/                    ← 🔧 CONFIGURATION FILES
│   ├── __init__.py
│   ├── env_config.json           ← URLs, usernames, passwords
│   └── execution_config.json     ← Browser settings (headless, viewport)
│
├── 📁 core/                      ← 🔨 FRAMEWORK UTILITIES
│   ├── __init__.py
│   └── config_reader.py          ← Reads config files
│
├── 📁 features/                  ← 📝 TEST SCENARIOS (Human-readable)
│   ├── login.feature             ← Feature file with scenarios
│   └── (add more features here)
│
├── 📁 pages/                     ← 🏠 PAGE OBJECTS (Website elements)
│   ├── __init__.py
│   ├── login_page.py             ← Defines login page locators & methods
│   └── (add more page objects)
│
├── 📁 step_definitions/          ← ⚙️ STEP IMPLEMENTATIONS
│   ├── __init__.py
│   ├── login_steps.py            ← Implements Given/When/Then steps
│   └── (add more step definitions)
│
├── 📁 tests/                     ← 🧪 TEST RUNNERS
│   ├── __init__.py
│   └── test_runner.py            ← Main file that runs all tests
│
├── 📁 __pycache__/               ← (Auto-generated, ignore this)
├── 📁 venv/                      ← (Your Python virtual environment)
│
├── conftest.py                   ← 🔌 Pytest configuration & fixtures
├── pytest.ini                    ← Pytest settings
├── requirements.txt              ← List of all dependencies
└── README.md                     ← This file!
```

### What Each Folder Does:

| Folder | Purpose | Example |
|--------|---------|---------|
| **config/** | Settings for different environments | QA URLs, test usernames |
| **core/** | Reusable framework code | Read config files |
| **features/** | What to test (human language) | "User should be able to login" |
| **pages/** | How to interact with website | "Click login button" |
| **step_definitions/** | Connect features to code | Implement "Click login button" |
| **tests/** | Run everything together | Run all tests |

---

## ⚙️ Configuration Setup

### File 1: `config/env_config.json`

This file contains **environment-specific settings** like URLs and credentials.

```json
{
  "env": "qa",
  "base_url": "https://practicetestautomation.com/practice-test-login/",
  "credentials": {
    "valid": {
      "username": "student",
      "password": "Password123"
    },
    "invalid": {
      "username": "invalid_user",
      "password": "wrong_password"
    }
  },
  "timeouts": {
    "page_load": 30000,
    "element": 10000
  }
}
```

**What each setting means:**
- `env`: Which environment ("qa", "prod", "dev")
- `base_url`: The website URL to test
- `credentials`: Login usernames and passwords
- `timeouts`: How long to wait for page/elements (in milliseconds)

### File 2: `config/execution_config.json`

This file contains **how to run tests**.

```json
{
  "browser": "chromium",
  "headless": false,
  "slow_mo": 0,
  "viewport": {
    "width": 1280,
    "height": 720
  },
  "retries": 1,
  "parallel_workers": 4,
  "record_video": false,
  "trace": false
}
```

**What each setting means:**
- `browser`: "chromium" (Chrome), "firefox", or "webkit" (Safari)
- `headless`: `true` = invisible browser, `false` = see the browser
- `slow_mo`: Delay between actions in milliseconds (0 = instant)
- `viewport`: Screen size (width x height)
- `retries`: Retry failed tests this many times
- `record_video`: Save video of test runs (requires disk space)
- `trace`: Record detailed trace (for debugging)

### Changing Configuration

**To see the browser while tests run:**
1. Open `config/execution_config.json`
2. Change `"headless": false`
3. Save and run tests

```json
{
  "browser": "chromium",
  "headless": false,  ← Change to false
  ...
}
```

**To slow down tests for watching:**
```json
{
  ...
  "slow_mo": 1000,  ← Add 1-second delay between actions
  ...
}
```

---

## ✍️ Your First Test

### Understanding the Flow

Here's how a test works:

```
Feature File (Human language)
        ↓
    Scenario: User logs in
    ├─ Given user is on the login page
    ├─ When user enters username and password
    └─ Then user should be logged in
        ↓
Step Definition (Python code)
        ↓
Page Object (Interact with website)
        ↓
Browser executes actions
```

---

### File 1: Feature File (`features/login.feature`)

This is the **"What to test"** written in human language.

```gherkin
Feature: User Login functionality

  Scenario: Successful login with valid credentials
    Given user is on the login page
    When user enters valid username and password
    And user clicks on login button
    Then user should be logged in successfully

  Scenario: Login fails with invalid credentials
    Given user is on the login page
    When user enters invalid username and password
    And user clicks on login button
    Then error should be displayed
```

**What this means:**
- **Feature**: What you're testing (login functionality)
- **Scenario**: A specific test case
- **Given**: The starting state (page is open)
- **When**: What the user does (enters username)
- **Then**: What should happen (success message shows)

---

### File 2: Page Object (`pages/login_page.py`)

This defines **how to interact with the website**.

```python
from playwright.sync_api import Page, expect

class LoginPage:
    """Page object for the login page"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # Element selectors (how to find elements on page)
        self.username_input = "#username"       # CSS selector for username field
        self.password_input = "#password"       # CSS selector for password field
        self.login_button = "#submit"           # CSS selector for login button
        self.success_message = "text=Logged In Successfully"  # Find by text
        self.error_message = ".login-error"     # Find by CSS class

    def open(self, url: str):
        """Navigate to the login page"""
        self.page.goto(url, wait_until="networkidle")
        print(f"✓ Opened {url}")

    def enter_username(self, username: str):
        """Enter username in the username field"""
        username_field = self.page.locator(self.username_input)
        expect(username_field).to_be_visible()  # Wait for field to appear
        username_field.fill(username)
        print(f"✓ Entered username: {username}")

    def enter_password(self, password: str):
        """Enter password in the password field"""
        password_field = self.page.locator(self.password_input)
        expect(password_field).to_be_visible()  # Wait for field to appear
        password_field.fill(password)
        print(f"✓ Entered password")

    def click_login(self):
        """Click the login button"""
        login_btn = self.page.locator(self.login_button)
        expect(login_btn).to_be_enabled()  # Wait for button to be clickable
        login_btn.click()
        print(f"✓ Clicked login button")

    def is_login_successful(self) -> bool:
        """Check if login succeeded by looking for success message"""
        try:
            success = self.page.locator(self.success_message)
            result = success.is_visible(timeout=5000)
            print(f"✓ Login successful: {result}")
            return result
        except Exception as e:
            print(f"✗ Error checking login success: {e}")
            return False

    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        try:
            error = self.page.locator(self.error_message)
            result = error.is_visible(timeout=5000)
            print(f"✓ Error displayed: {result}")
            return result
        except Exception:
            # If no specific error element, check that success wasn't shown
            return not self.is_login_successful()
```

---

### File 3: Step Definitions (`step_definitions/login_steps.py`)

This connects the **human language** to **Python code**.

```python
from pytest_bdd import given, when, then
from pages.login_page import LoginPage

# ==================== GIVEN (Setup/Initial State) ====================

@given('user is on the login page')
def given_user_on_login_page(page, env_config):
    """Navigate to the login page"""
    login_page = LoginPage(page)
    login_page.open(env_config["base_url"])

# ==================== WHEN (User Actions) ====================

@when('user enters valid username and password')
def when_user_enters_valid_credentials(page, env_config):
    """Enter valid username and password from config"""
    login_page = LoginPage(page)
    credentials = env_config["credentials"]["valid"]
    login_page.enter_username(credentials["username"])
    login_page.enter_password(credentials["password"])

@when('user enters invalid username and password')
def when_user_enters_invalid_credentials(page, env_config):
    """Enter invalid username and password"""
    login_page = LoginPage(page)
    credentials = env_config["credentials"]["invalid"]
    login_page.enter_username(credentials["username"])
    login_page.enter_password(credentials["password"])

@when('user clicks on login button')
def when_user_clicks_login(page):
    """Click the login button"""
    login_page = LoginPage(page)
    login_page.click_login()

# ==================== THEN (Verification) ====================

@then('user should be logged in successfully')
def then_user_should_be_logged_in(page):
    """Verify user is logged in"""
    login_page = LoginPage(page)
    assert login_page.is_login_successful(), "✗ Login failed - success message not shown"
    print("✓ Test passed: User is logged in")

@then('error should be displayed')
def then_error_should_be_displayed(page):
    """Verify error message is displayed"""
    login_page = LoginPage(page)
    assert login_page.is_error_displayed(), "✗ Error message not displayed"
    print("✓ Test passed: Error is displayed")
```

---

### File 4: Test Runner (`tests/test_runner.py`)

This file **loads all features and steps**.

```python
from pytest_bdd import scenarios
# Import all step definitions to make them available
from step_definitions.login_steps import *  # noqa: F401, F403

# Load all scenarios from the feature file
scenarios("../features/login.feature")
```

**What it does:**
- Imports all step definitions
- Loads all scenarios from feature files
- Pytest automatically creates test functions from scenarios

---

## 🧪 Running Tests

### Run All Tests

```bash
python -m pytest -q
```

**Output:**
```
tests\test_runner.py ..  [100%]
2 passed in 9.40s
```

✅ Both tests passed!

---

### Run Tests in Verbose Mode (See Details)

```bash
python -m pytest -v
```

Shows each step being executed.

---

### Run Only One Scenario

**Method 1: Using Tags** (Recommended)

Add a tag to your scenario:
```gherkin
@focus  ← Add this
Scenario: Successful login with valid credentials
```

Then run:
```bash
python -m pytest -m focus -q
```

**Method 2: Run by Name**
```bash
python -m pytest tests/test_runner.py::test_successful_login_with_valid_credentials -q
```

---

### Run Tests with Browser Visible

Edit `config/execution_config.json`:
```json
{
  "browser": "chromium",
  "headless": false,  ← Change this
  ...
}
```

Then run tests - you'll see the browser open and interact with the website!

---

### Run Tests Slowly (To Watch Actions)

Edit `config/execution_config.json`:
```json
{
  ...
  "slow_mo": 1000,  ← Add 1 second delay between actions
  ...
}
```

---

### Run Tests by Category

Add markers to your scenarios:
```gherkin
@smoke
Scenario: Login works
  ...

@regression
Scenario: Login fails with invalid credentials
  ...
```

Run only smoke tests:
```bash
python -m pytest -m smoke -q
```

Run only regression tests:
```bash
python -m pytest -m regression -q
```

---

## 🚀 Advanced Commands & Common Tasks

### 1️⃣ Run Specific Test Suites (Smoke, Regression, etc.)

#### Add Tags to Your Scenarios

Edit `features/login.feature`:
```gherkin
Feature: Login functionality

  @smoke @regression
  Scenario: Successful login with valid credentials
    Given user is on the login page
    When user enters valid username and password
    And user clicks on login button
    Then user should be logged in successfully

  @regression @sanity
  Scenario: Login fails with invalid credentials
    Given user is on the login page
    When user enters invalid username and password
    And user clicks on login button
    Then error should be displayed
```

#### Run Commands

**Run ONLY @smoke tests:**
```bash
python -m pytest -m smoke -q
```

**Run ONLY @regression tests:**
```bash
python -m pytest -m regression -q
```

**Run ONLY @sanity tests:**
```bash
python -m pytest -m sanity -q
```

**Run @smoke AND @regression tests:**
```bash
python -m pytest -m "smoke or regression" -q
```

**Run @regression but NOT @sanity:**
```bash
python -m pytest -m "regression and not sanity" -q
```

**Run ALL tests EXCEPT @focus (development tag):**
```bash
python -m pytest -m "not focus" -q
```

#### Define Available Markers

Markers are already defined in `pytest.ini`:
```ini
markers =
    smoke: Smoke tests - quick sanity checks
    regression: Regression tests - full test suite
    Sanity: Sanity tests - basic functionality
    focus: Run only this scenario (development only)
```

**Add your own markers to pytest.ini:**
```ini
markers =
    smoke: Smoke tests
    regression: Full regression
    sanity: Basic functionality
    critical: Critical functionality
    ui: UI tests
    api: API tests
```

Then use in features:
```gherkin
@critical @ui
Scenario: Important user flow
```

And run:
```bash
python -m pytest -m critical -q
python -m pytest -m ui -q
```

---

### 2️⃣ Trace Failed Test Cases (Debugging)

#### Enable Trace Recording

**Step 1:** Edit `config/execution_config.json`
```json
{
  "browser": "chromium",
  "headless": false,
  "slow_mo": 0,
  "viewport": {
    "width": 1280,
    "height": 720
  },
  "trace": true  ← Change to true
}
```

**Step 2:** Run tests
```bash
python -m pytest -q
```

A `trace.zip` file will be created in the project root.

#### View the Trace Recording

**Method 1: Using Playwright Inspector (Interactive)**
```bash
python -m playwright show-trace trace.zip
```

This opens a visual debugger showing:
- ✅ Every action (click, type, navigate)
- ✅ Screenshots before/after each action
- ✅ Network requests
- ✅ Console logs and errors
- ✅ Exact timing of each step

**Method 2: Online Viewer (No Installation)**
1. Go to: https://trace.playwright.dev/
2. Drag and drop your `trace.zip` file
3. View everything visually

#### File Location

```
C:\PythonWorkspace\playwright-bdd\trace.zip
```

Open in File Explorer:
```bash
explorer C:\PythonWorkspace\playwright-bdd\trace.zip
```

#### Run Failed Tests Only with Trace

**Get last failed test name:**
```bash
python -m pytest --lf -q
```

**Run last failed test with trace enabled:**
```bash
python -m pytest --lf -q
```

**Run specific failed test:**
```bash
python -m pytest tests/test_runner.py::test_login_failed_with_invalid_login_credentials -q
```

#### Save Multiple Traces

Before running tests again, rename the previous trace:
```bash
Rename-Item trace.zip "trace_login_$(Get-Date -Format 'yyyyMMdd_HHmmss').zip"
python -m pytest -q
```

This creates files like:
```
trace_login_20251226_144530.zip
trace_login_20251226_145045.zip
```

#### Disable Trace (To Speed Up Tests)

When you're done debugging, turn off trace:
```json
{
  ...
  "trace": false  ← Change back to false
}
```

This will speed up test execution and not create large trace files.

---

### 3️⃣ Parallel Execution (Run Multiple Tests Simultaneously)

#### Install Parallel Plugin

```bash
python -m pip install pytest-xdist
```

(Already included in `requirements.txt`)

#### Configuration

Edit `config/execution_config.json` and set number of workers:
```json
{
  "browser": "chromium",
  "parallel_workers": 4  ← Number of parallel threads
}
```

#### Run Tests in Parallel

**Run with 4 parallel workers:**
```bash
python -m pytest -n 4 -q
```

**Run with auto-detection (uses all CPU cores):**
```bash
python -m pytest -n auto -q
```

**Run with 2 parallel workers:**
```bash
python -m pytest -n 2 -q
```

#### Parallel Execution Examples

**Run all tests in parallel (4 workers):**
```bash
python -m pytest -n 4 -q
```

**Run @smoke tests in parallel (2 workers):**
```bash
python -m pytest -m smoke -n 2 -q
```

**Run @regression tests in parallel (auto):**
```bash
python -m pytest -m regression -n auto -q
```

**Run verbose output with parallel (2 workers):**
```bash
python -m pytest -n 2 -v
```

#### Expected Output

Without parallel:
```
test_runner.py ..  [100%]
2 passed in 9.40s
```

With parallel (4 workers):
```
test_runner.py ..  [100%]
2 passed in 3.20s  ← Much faster!
```

#### Important Notes for Parallel Execution

⚠️ **Things to consider:**
1. **Browser instances** - Each worker gets its own browser
2. **Port conflicts** - Make sure ports aren't hardcoded
3. **Database** - Use unique test data for each worker
4. **File conflicts** - Each worker should use separate output files

✅ **Best practices:**
```bash
# Use markers to run specific subsets in parallel
python -m pytest -m smoke -n auto -q

# Don't use -n with trace (trace slows down parallel)
# First debug with trace off, then run parallel

# Run sequential for debugging, parallel for regression
python -m pytest -q              # Sequential (slow, good for debugging)
python -m pytest -n auto -q      # Parallel (fast, for CI/CD)
```

---

## 📊 Quick Command Reference

### Test Execution
```bash
# Run all tests
python -m pytest -q

# Run with details
python -m pytest -v

# Run specific test by name
python -m pytest tests/test_runner.py::test_successful_login_with_valid_credentials -q

# Run last failed test
python -m pytest --lf -q

# Run failed tests (from last run)
python -m pytest --failed-first -q
```

### Run by Markers
```bash
# Smoke tests only
python -m pytest -m smoke -q

# Regression tests only
python -m pytest -m regression -q

# Smoke OR Regression
python -m pytest -m "smoke or regression" -q

# Regression but NOT sanity
python -m pytest -m "regression and not sanity" -q

# Everything except focus (development)
python -m pytest -m "not focus" -q
```

### Parallel Execution
```bash
# Run with 4 workers
python -m pytest -n 4 -q

# Run with all CPU cores
python -m pytest -n auto -q

# Parallel + markers
python -m pytest -m smoke -n 4 -q
```

### Debugging & Tracing
```bash
# Enable trace in config first: "trace": true

# Run tests (creates trace.zip)
python -m pytest -q

# View trace in visual inspector
python -m playwright show-trace trace.zip

# Or upload to online viewer: https://trace.playwright.dev/
```

### Browser Control
```bash
# Run tests with visible browser (set headless: false in config)
python -m pytest -q

# Slow down tests (set slow_mo: 1000 in config)
python -m pytest -q

# Run in different browser
# Edit config: "browser": "firefox"  or  "webkit"
python -m pytest -q
```

---

## 🎯 Real-World Usage Examples

### Scenario 1: Quick Smoke Test (CI/CD Pipeline)
```bash
python -m pytest -m smoke -n auto -q
```
- Runs only @smoke tests
- Uses all CPU cores (fast)
- Quiet output (no details)
- Perfect for quick validation

### Scenario 2: Full Regression Test Suite
```bash
python -m pytest -m regression -q
```
- Runs all @regression tests
- Sequential execution (one at a time)
- Good for thorough testing
- Takes longer but more reliable

### Scenario 3: Debug Single Failing Test
```bash
# Edit config: "trace": true, "headless": false, "slow_mo": 1000
python -m pytest tests/test_runner.py::test_login_failed_with_invalid_login_credentials -v
python -m playwright show-trace trace.zip
```
- See browser interactions
- Slow down to watch actions
- Record trace for debugging
- View detailed trace recording

### Scenario 4: Local Development (Focus on One Test)
```gherkin
@focus  ← Add to your scenario
Scenario: Working on this feature
```
```bash
python -m pytest -m focus -q
```
- Run only your test
- Fast feedback loop
- Remove @focus before committing

### Scenario 5: Pre-Commit Testing
```bash
python -m pytest -m "not focus" -n auto -q
```
- Run all tests except development (@focus)
- Parallel execution
- Quick validation before committing

---

## ✏️ Writing More Tests

### Create a New Feature File

1. Create `features/payment.feature`:
```gherkin
Feature: Payment Processing

  @smoke
  Scenario: Complete payment successfully
    Given user is on the payment page
    When user enters valid card details
    And user clicks pay button
    Then payment should be processed successfully
```

2. Create `pages/payment_page.py`:
```python
from playwright.sync_api import Page, expect

class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        self.card_input = "#card-number"
        self.pay_button = "#submit-payment"
        self.success_message = "text=Payment Successful"

    def open(self, url: str):
        self.page.goto(url)

    def enter_card_details(self, card: str):
        card_field = self.page.locator(self.card_input)
        expect(card_field).to_be_visible()
        card_field.fill(card)

    def click_pay(self):
        pay_btn = self.page.locator(self.pay_button)
        expect(pay_btn).to_be_enabled()
        pay_btn.click()

    def is_payment_successful(self) -> bool:
        try:
            success = self.page.locator(self.success_message)
            return success.is_visible(timeout=5000)
        except Exception:
            return False
```

3. Create `step_definitions/payment_steps.py`:
```python
from pytest_bdd import given, when, then
from pages.payment_page import PaymentPage

@given('user is on the payment page')
def given_payment_page(page, env_config):
    payment_page = PaymentPage(page)
    payment_page.open(env_config["base_url"] + "/payment")

@when('user enters valid card details')
def when_enters_card_details(page, env_config):
    payment_page = PaymentPage(page)
    payment_page.enter_card_details(env_config["credentials"]["card"])

@when('user clicks pay button')
def when_clicks_pay(page):
    payment_page = PaymentPage(page)
    payment_page.click_pay()

@then('payment should be processed successfully')
def then_payment_successful(page):
    payment_page = PaymentPage(page)
    assert payment_page.is_payment_successful(), "Payment failed"
```

4. Update `tests/test_runner.py`:
```python
from pytest_bdd import scenarios
from step_definitions.login_steps import *  # noqa: F401, F403
from step_definitions.payment_steps import *  # noqa: F401, F403

scenarios("../features/login.feature")
scenarios("../features/payment.feature")  ← Add this
```

5. Run tests:
```bash
python -m pytest -q
```

---

## 🐛 Common Issues & Solutions

### Issue 1: "Python not found"
**Problem:** You see `python : The term 'python' is not recognized`

**Solution:**
- Reinstall Python
- ✅ **IMPORTANT**: Check "Add Python to PATH" during installation
- Restart your terminal

---

### Issue 2: "ModuleNotFoundError: No module named 'pytest'"
**Problem:** Pytest is not installed

**Solution:**
```bash
# Make sure venv is activated
python -m pip install -r requirements.txt
```

---

### Issue 3: Tests can't find step definitions
**Problem:** `StepDefinitionNotFoundError`

**Solution:**
- Check that `tests/test_runner.py` imports your step file:
  ```python
  from step_definitions.my_steps import *
  ```
- Ensure step file name is correct in the import
- Make sure step text matches exactly (case-sensitive!)

---

### Issue 4: Browser doesn't launch
**Problem:** Tests run but no browser window appears

**Solution:**
- Check `execution_config.json` - `headless` should be `false`
- Reinstall Playwright: `python -m playwright install`
- Check browser isn't hidden behind other windows

---

### Issue 5: "Timeout waiting for element"
**Problem:** Test fails because element can't be found

**Solutions:**
- Increase timeout in `env_config.json`:
  ```json
  "timeouts": {
    "element": 20000  ← Increase from 10000
  }
  ```
- Check your CSS selector is correct
- Wait for page to fully load: `page.goto(url, wait_until="networkidle")`

---

### Issue 6: "Connection refused"
**Problem:** Tests fail trying to connect to website

**Solutions:**
- Check `base_url` in `config/env_config.json`
- Make sure the website is online
- Check your internet connection
- Check firewall settings

---

## 🎯 Best Practices

### 1. **Use Meaningful Names**
✅ Good:
```python
def test_user_can_login_with_valid_credentials():
```

❌ Bad:
```python
def test1():
```

### 2. **One Assertion Per Step**
✅ Good:
```python
@then('user should be logged in successfully')
def then_login_success(page):
    login_page = LoginPage(page)
    assert login_page.is_login_successful()
```

❌ Bad:
```python
@then('user should be logged in successfully')
def then_login_success(page):
    login_page = LoginPage(page)
    assert login_page.is_login_successful()
    assert login_page.user_name_visible()
    assert login_page.logout_button_visible()
```

### 3. **Reuse Steps**
✅ Good - same step for multiple scenarios:
```gherkin
Scenario: Login works
  Given user is on the login page  ← Reused
  When user enters valid credentials
  Then user should be logged in

Scenario: Logout works
  Given user is on the login page  ← Same step!
  When user clicks logout
  Then user should see login form
```

### 4. **Use Page Objects**
✅ Good - all element selectors in one place:
```python
class LoginPage:
    def __init__(self, page):
        self.username_input = "#username"  ← All selectors here
        self.password_input = "#password"
```

❌ Bad - selectors scattered everywhere:
```python
@when('user enters username')
def step(page):
    page.fill("#username", "test")  ← Selector here
```

### 5. **Manage Test Data in Config**
✅ Good:
```json
{
  "credentials": {
    "valid": {
      "username": "student",
      "password": "Password123"
    }
  }
}
```

❌ Bad:
```python
login_page.enter_username("hardcoded_username")
```

### 6. **Clear Error Messages**
✅ Good:
```python
assert login_page.is_login_successful(), "Login failed - success message not visible after 10 seconds"
```

❌ Bad:
```python
assert login_page.is_login_successful()
```

### 7. **Use Explicit Waits**
✅ Good - waits for element to be ready:
```python
expect(username_field).to_be_visible()
username_field.fill(username)
```

❌ Bad - hardcoded delay:
```python
time.sleep(5)
username_field.fill(username)
```

---

## 📖 Glossary

| Term | Definition | Example |
|------|-----------|---------|
| **BDD** | Behavior-Driven Development - testing written in human language | "User should be able to login" |
| **Gherkin** | The language used to write BDD tests | Given/When/Then |
| **Feature File** | File containing test scenarios (`.feature`) | `login.feature` |
| **Scenario** | A single test case | "User logs in successfully" |
| **Step** | One action in a scenario | "user enters username" |
| **Page Object** | Class representing a webpage | `LoginPage` |
| **Locator** | How to find an element on a page | `"#username"` (CSS selector) |
| **Fixture** | Reusable test setup | `page`, `env_config` |
| **pytest** | Python testing framework | `pytest -q` |
| **Playwright** | Browser automation library | Controls browser, clicks, types |
| **Headless** | Running browser invisibly | `"headless": true` |
| **Viewport** | Browser window size | 1280 x 720 pixels |

---

## 📚 Useful Resources

**Learning:**
- [Playwright Docs](https://playwright.dev/python/) - How to interact with browsers
- [pytest-bdd Docs](https://pytest-bdd.readthedocs.io/) - BDD framework
- [Gherkin Guide](https://cucumber.io/docs/gherkin/) - How to write scenarios
- [CSS Selectors](https://www.w3schools.com/cssref/selectors_class.asp) - Finding elements

**Tools:**
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Inspect elements and find selectors
- [VS Code](https://code.visualstudio.com/) - Code editor
- [Pytest Documentation](https://docs.pytest.org/) - Testing framework

---

## ❓ Quick Reference

### Commands You'll Use Most

```bash
# Activate virtual environment
& venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install -r requirements.txt

# Run all tests
python -m pytest -q

# Run tests with details
python -m pytest -v

# Run only one scenario
python -m pytest -m focus -q

# Run tests by marker
python -m pytest -m smoke -q

# Update Playwright
python -m playwright install
```

---

## 🎓 Learning Path

**Day 1:**
- [ ] Install Python and virtual environment
- [ ] Run existing tests
- [ ] Understand project structure

**Day 2:**
- [ ] Read a feature file
- [ ] Understand step definitions
- [ ] Look at page object

**Day 3:**
- [ ] Modify an existing test
- [ ] Change a step definition
- [ ] Update config values

**Day 4:**
- [ ] Write a new feature file
- [ ] Create a new page object
- [ ] Implement steps

**Day 5:**
- [ ] Write multiple scenarios
- [ ] Use tags to run specific tests
- [ ] Generate reports

---

## 🎉 You're Ready!

You now understand:
- ✅ How this framework works
- ✅ How to run tests
- ✅ How to write tests
- ✅ How to fix problems

**Start with:**
```bash
python -m pytest -q
```

Then explore the code and start building your own tests!

---

## 💬 Still Have Questions?

Common questions answered:

**Q: Where do I find element selectors?**
A: Right-click on element → Inspect → Look for `id=`, `class=`, or unique text

**Q: How do I slow down tests?**
A: Edit `execution_config.json` and change `"slow_mo": 1000`

**Q: Can I run tests in parallel?**
A: Yes! Update `parallel_workers` in `execution_config.json`

**Q: How do I debug a failing test?**
A: Run with `python -m pytest -v` to see detailed output

**Q: Can I test multiple browsers?**
A: Yes! Change `"browser": "firefox"` in `execution_config.json`

---

**Last Updated:** December 26, 2025
**Framework Version:** 1.0 - Production Ready
**Status:** ✅ Ready to Use
