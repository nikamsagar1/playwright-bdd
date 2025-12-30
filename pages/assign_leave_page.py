from playwright.sync_api import Page

class AssignLeavePage:

    def __init__(self, page: Page):
        self.page = page

    def assign_leave(self, employee_name: str):
        # Employee name
        self.page.locator("input[placeholder='Type for hints...']").fill(employee_name)
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Leave Type
        self.page.locator("div.oxd-select-text").nth(0).click()
        self.page.locator("span:has-text('CAN - Vacation')").click()

        # From Date
        self.page.locator("input[placeholder='yyyy-mm-dd']").nth(0).fill("2025-01-15")

        # To Date
        self.page.locator("input[placeholder='yyyy-mm-dd']").nth(1).fill("2025-01-16")

        # Assign button
        self.page.locator("button:has-text('Assign')").click()

        # Confirm popup
        self.page.locator("button:has-text('Ok')").click()

    def is_success_message_displayed(self) -> bool:
        return self.page.locator("p:has-text('Successfully Assigned')").is_visible()
