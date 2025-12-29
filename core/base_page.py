# core/base_page.py
from playwright.sync_api import Page, Locator, expect

class BasePage:
    """
    BasePage defines standard UI actions for all page classes.

    All page classes MUST inherit from BasePage.
    This ensures:
    - Consistent waits
    - Centralized assertions
    - No duplicate Playwright code across pages
    """

    def __init__(self, page: Page):
        """
        Initialize BasePage with a Playwright Page object.

        :param page: Playwright Page object provided by PageFactory
        """
        self.page = page

    # --------------------
    # Navigation
    # --------------------
    def navigate(self, url: str):
        """Navigate to the given URL."""
        self.page.goto(url)

    # --------------------
    # Element Actions
    # --------------------
    def click(self, locator: Locator):
        """
        Click on element after ensuring it is visible.

        :param locator: Playwright Locator object
        """
        expect(locator).to_be_visible()
        locator.click()

    def fill(self, locator: Locator, value: str):
        """
        Fill input field after ensuring it is visible.

        :param locator: Playwright Locator object
        :param value: Value to fill into the input field
        """
        expect(locator).to_be_visible()
        locator.fill(value)

    def get_text(self, locator: Locator) -> str:
        """
        Get visible text from element.

        :param locator: Playwright Locator object
        :return: Text content of the element
        """
        expect(locator).to_be_visible()
        return locator.inner_text()

    # --------------------
    # Assertions
    # --------------------
    def assert_visible(self, locator: Locator):
        """Assert that element is visible."""
        expect(locator).to_be_visible()

    def assert_text(self, locator: Locator, expected_text: str):
        """Assert that element text matches expected value."""
        expect(locator).to_have_text(expected_text)

    # --------------------
    # Waits
    # --------------------
    def wait_for_visible(self, locator: Locator):
        """Wait until element becomes visible."""
        expect(locator).to_be_visible()
