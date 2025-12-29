# core/app_context.py

from core.config_reader import ConfigReader
from core.browser_manager import BrowserManager
from core.page_factory import PageFactory
import os
from datetime import datetime


class AppContext:
    """
    AppContext is created ONCE per test scenario.
    It manages browser lifecycle, configuration, and page objects.

    Key Responsibilities:
    - Open browser once per scenario
    - Load configuration once
    - Provide reusable page objects via PageFactory
    - Close browser cleanly after scenario
    - Capture screenshots on failure
    """

    def __init__(self, env: str | None = None, screenshot_dir: str = "screenshots"):
        """
        Initialize AppContext.

        :param env: Environment name (qa, uat, prod). Defaults to 'qa' if not provided.
        :param screenshot_dir: Directory to save screenshots
        """
        # Default to 'qa' if env is not provided
        self.env = env or "qa"
        print(f"[AppContext] Environment: {self.env}")
        
        # Load configurations (env + execution)
        self.env_config = ConfigReader.get_env_config()
        self.execution_config = ConfigReader.get_execution_config()

        # Browser & page objects
        self.browser = None
        self.page = None

        # Managers
        self.browser_manager = BrowserManager(self.execution_config)
        self.page_factory = None

        # Directory for screenshots
        self.screenshot_dir = screenshot_dir
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def setup(self, base_url: str):
        """
        Launch the browser and open the base URL.

        :param base_url: URL to navigate at start of test
        """
        # Launch browser and create page
        self.browser, self.page = self.browser_manager.launch_browser(base_url=base_url)

        # Initialize PageFactory with the page
        self.page_factory = PageFactory(self.page)

    def get_page(self, page_class):
        """
        Returns a cached page object (singleton per scenario).

        Example:
            login_page = app_context.get_page(LoginPage)

        :param page_class: Class of the page object
        """
        if not self.page_factory:
            raise Exception("AppContext not setup yet. Call setup() first.")
        return self.page_factory.get_page(page_class)

    def teardown(self, capture_screenshot: bool = True, test_name: str = "test"):
        """
        Close browser cleanly after scenario.
        Optionally capture screenshot if scenario failed.

        :param capture_screenshot: Whether to capture screenshot
        :param test_name: Name of the test scenario (used in screenshot filename)
        """
        if self.browser:
            if capture_screenshot and self.page:
                try:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    screenshot_file = os.path.join(
                        self.screenshot_dir, f"{test_name}_{timestamp}.png"
                    )
                    self.page.screenshot(path=screenshot_file)
                    print(f"[AppContext] Screenshot saved: {screenshot_file}")
                except Exception as e:
                    print(f"[AppContext] Failed to capture screenshot: {e}")
            self.browser_manager.close_browser()
