class UsersPage:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator('//button[text()=" Add "]')
        self.user_table = page.locator('//div[@role="row"]')

    def click_add_user(self):
        self.add_button.click()

    def is_user_present(self, username):
        return self.page.locator(f'//div[text()="{username}"]').is_visible()
