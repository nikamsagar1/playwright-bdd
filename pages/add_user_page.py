class AddUserPage:
    def __init__(self, page):
        self.page = page
        self.employee_name_input = page.locator('input[placeholder="Type for hints..."]')
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.confirm_password_input = page.locator('input[name="confirmPassword"]')
        self.save_button = page.locator('button[type="submit"]')

    def add_user(self, employee_name, username, password, confirm_password):
        self.employee_name_input.fill(employee_name)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)
        self.save_button.click()
