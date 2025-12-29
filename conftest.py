# conftest.py
import pytest
from core.app_context import AppContext
import os

# -----------------------------
# Pytest CLI options
# -----------------------------
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=None,
                     help="Environment to run tests against (qa, uat, prod)")
    parser.addoption("--headed", action="store_true",
                     help="Run browser in headed (visible) mode")


# -----------------------------
# Fixture: app_context
# -----------------------------
@pytest.fixture(scope="function")
def app_context(request):
    """
    Fixture that:
    1. Reads environment & execution config via ConfigReader
    2. Launches browser using BrowserManager
    3. Navigates to base URL
    4. Provides AppContext (with PageFactory) to step definitions
    5. Tears down browser cleanly and captures screenshot if test failed
    """
    # Get environment from CLI (AppContext will default to 'qa' if not provided)
    env = request.config.getoption("--env")
    context = AppContext(env=env)

    # Get the base URL for the selected environment (use context.env which has the default applied)
    env_config = context.env_config.get("environments", {}).get(context.env, {})
    base_url = env_config.get("base_url", "http://localhost")
    context.setup(base_url)

    # Provide AppContext to test/step definitions
    yield context

    # Teardown after test
    test_name = request.node.name
    failed = getattr(request.node, "rep_call", None)
    failed = failed.failed if failed else False
    context.teardown(capture_screenshot=failed, test_name=test_name)


# -----------------------------
# Hook: attach test result for screenshot handling
# -----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach test result (pass/fail) to test item
    so fixtures can detect failures and capture screenshots
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# -----------------------------
# Optional: Ensure HTML report directory exists
# -----------------------------
def pytest_configure(config):
    html_path = config.getoption("--html")
    if html_path:
        os.makedirs(os.path.dirname(html_path), exist_ok=True)
