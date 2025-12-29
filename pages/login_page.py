from playwright.sync_api import Page

class LoginPage:
    """
    Page Object Model (POM) class for the Login Page of the application.

    POM Type:
    - This is an example of a **Page Object Class / Standard POM**.
    - Encapsulates the elements (locators) and actions (methods) of the login page.
    - Does NOT contain test logic; test/step definitions interact with this class.

    Responsibilities:
    - Define locators for UI elements
    - Define methods to interact with these elements (actions)
    """

    def __init__(self, page: Page):
        """
        Initialize LoginPage with a Playwright Page instance.

        :param page: Playwright Page object (from AppContext / PageFactory)
        """
        self.page = page

        # --------------------
        # Locators for the login page
        # --------------------
        self.username_input = page.locator('input[name="username"]')  # Username field
        self.password_input = page.locator('input[name="password"]')  # Password field
        self.login_button = page.locator('button[type="submit"]')     # Login button

    # --------------------
    # Actions / Methods
    # --------------------
    def login(self, username: str, password: str):
        """
        Perform login action using given username and password.

        Steps:
        1. Fill the username input
        2. Fill the password input
        3. Click the login button

        :param username: User's username
        :param password: User's password
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
