# Quick Start Guide - Get Started in 5 Minutes

## What You Need

- Python 3.10+
- Git
- Text Editor (VS Code recommended)

## Step 1: Setup (First Time Only)

```bash
# Navigate to project folder
cd c:\PythonWorkspace\playwright-bdd

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install browsers
playwright install
```

## Step 2: Add Your First Test

### Create a Feature File
Create file: `features/my_test.feature`

```gherkin
Feature: My First Test

  Scenario: Simple login test
    Given user is on the login page
    When user enters username "Admin"
    And user enters password "admin123"
    And user clicks login button
    Then user is logged in successfully
```

### Create Step Definitions
Create file: `step_definitions/my_test_steps.py`

```python
from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@given("user is on the login page")
def user_on_login_page(app_context):
    """User navigates to login page"""
    login_page = app_context.get_page(LoginPage)
    return login_page

@when('user enters username "<username>"')
def enter_username(app_context, username):
    """Enter username"""
    login_page = app_context.get_page(LoginPage)
    login_page.enter_username(username)

@when('user enters password "<password>"')
def enter_password(app_context, password):
    """Enter password"""
    login_page = app_context.get_page(LoginPage)
    login_page.enter_password(password)

@when("user clicks login button")
def click_login(app_context):
    """Click login"""
    login_page = app_context.get_page(LoginPage)
    login_page.click_login()

@then("user is logged in successfully")
def verify_login(app_context):
    """Verify login success"""
    dashboard = app_context.get_page(DashboardPage)
    assert dashboard.is_logged_in(), "Login failed"
```

## Step 3: Update test_runner.py

Edit: `tests/test_runner.py`

```python
from pytest_bdd import scenarios
from step_definitions.my_test_steps import *

# Load your new feature file
scenarios("../features/my_test.feature")
```

## Step 4: Run Your Test

```bash
# Run test
pytest tests/test_runner.py --env=qa --headed

# Run with report
pytest tests/test_runner.py --env=qa --html=reports/report.html

# View report
start reports/report.html
```

## Common Issues

### "Module not found"
```bash
# Make sure you're in virtual environment
venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### "Browser won't open"
```bash
# Reinstall Playwright
playwright install

# Check if port is available
```

### "Element not found"
```
1. Open page manually in headed mode
2. Inspect element to get correct selector
3. Update locator in page class
```

## Directory Structure to Remember

```
features/          ← Put .feature files here
step_definitions/  ← Put _steps.py files here
pages/             ← Put page classes here
tests/             ← Main test runner
```

## Command Cheat Sheet

```bash
# Run all tests
pytest tests/test_runner.py -v

# Run in QA environment
pytest tests/test_runner.py --env=qa

# See browser
pytest tests/test_runner.py --headed

# Generate report
pytest tests/test_runner.py --html=reports/report.html

# Stop on first failure
pytest tests/test_runner.py -x

# Show print statements
pytest tests/test_runner.py -s

# Run specific test
pytest tests/test_runner.py -k "login" -v
```

## Next Steps

1. Read full [USER_GUIDE.md](USER_GUIDE.md)
2. Check [configuration files](config/)
3. Explore existing [page objects](pages/)
4. Write more feature files

---

**Need help?** See troubleshooting section in USER_GUIDE.md
