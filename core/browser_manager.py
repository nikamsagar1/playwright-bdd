# core/browser_manager.py
from playwright.sync_api import sync_playwright

class BrowserManager:
    """
    BrowserManager handles:
    - Launching the browser based on execution config
    - Creating a page
    - Applying headless, viewport, slow-mo settings
    - Closing browser cleanly
    """

    def __init__(self, execution_config):
        self.execution_config = execution_config
        self.playwright = None
        self.browser = None

    def launch_browser(self, base_url: str):
        self.playwright = sync_playwright().start()

        browser_type = self.execution_config.get("browser", "chromium")
        headless = self.execution_config.get("headless", True)
        slow_mo = self.execution_config.get("slow_mo", 0)
        viewport = self.execution_config.get("viewport", {"width": 1280, "height": 720})

        # Select browser type
        if browser_type == "chromium":
            browser_launcher = self.playwright.chromium
        elif browser_type == "firefox":
            browser_launcher = self.playwright.firefox
        elif browser_type == "webkit":
            browser_launcher = self.playwright.webkit
        else:
            raise ValueError(f"Unsupported browser: {browser_type}")

        # Launch browser
        self.browser = browser_launcher.launch(headless=headless, slow_mo=slow_mo)

        # Create page
        context = self.browser.new_context(viewport=viewport)
        page = context.new_page()

        # Navigate to base URL
        page.goto(base_url)

        return self.browser, page

    def close_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
