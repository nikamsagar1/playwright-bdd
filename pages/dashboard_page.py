class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.admin_tab = page.locator('//span[text()="Admin"]')

    def go_to_admin_tab(self):
        self.admin_tab.click()

    def click_assign_leave(self):
        self.page.locator("//button[@title='Assign Leave']").click()
