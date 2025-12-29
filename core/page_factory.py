# core/page_factory.py
from typing import Type

class PageFactory:
    """
    PageFactory is responsible for:
    - Creating page object instances
    - Caching them
    - Returning the SAME instance whenever requested

    This ensures:
    - Only one object per page class per test
    - Faster execution
    - Consistent page state across step definitions
    """

    def __init__(self, page):
        """
        Initialize PageFactory with a Playwright page or AppContext.

        :param page: Playwright Page object (or AppContext.page) created by BrowserManager
        """
        # Store the underlying Playwright page object
        self.page = page
        # Dictionary to cache page object instances
        self._page_instances = {}

    def get_page(self, page_class: Type) -> object:
        """
        Return a page object instance for the given page class.

        If the page object is already created:
        - Return the cached instance

        If not created:
        - Create it
        - Store it in cache
        - Return it

        :param page_class: The class of the page object (e.g., LoginPage)
        :return: Instance of the page class
        """
        if page_class not in self._page_instances:
            # Instantiate the page class with the current page
            self._page_instances[page_class] = page_class(self.page)

        return self._page_instances[page_class]
