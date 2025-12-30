from pytest_bdd import given, when, then
from pages.assign_leave_page import AssignLeavePage
from pages.dashboard_page import DashboardPage


@when("I click on Assign Leave from Quick Launch")
def click_assign_leave_from_quick_launch(app_context):
    dashboard_page = app_context.get_page(DashboardPage)
    dashboard_page.click_assign_leave()


@when('I assign leave to "Joy Smith"')
def assign_leave(app_context):
    assign_leave_page = app_context.get_page(AssignLeavePage)
    assign_leave_page.assign_leave("Joy Smith")


@then("the leave should be assigned successfully")
def verify_leave_assigned(app_context):
    assign_leave_page = app_context.get_page(AssignLeavePage)
    assert assign_leave_page.is_success_message_displayed()
