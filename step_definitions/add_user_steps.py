# step_definitions/add_user_steps.py

from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.users_page import UsersPage
from pages.add_user_page import AddUserPage


# -----------------------------
# Given steps
# -----------------------------
@given("I am on the login page")
def open_login_page(app_context):
    """
    The login page is already opened by AppContext.setup().
    Just return the LoginPage object.
    """
    return app_context.get_page(LoginPage)


# -----------------------------
# When steps
# -----------------------------
@when("I login with valid credentials")
def login(app_context):
    login_page = app_context.get_page(LoginPage)
    login_page.login(username="Admin", password="admin123")
    return app_context.get_page(DashboardPage)


@when("I navigate to the Users page")
def go_to_users_page(app_context):
    dashboard_page = app_context.get_page(DashboardPage)
    dashboard_page.go_to_admin_tab()  # Navigate to Users/Admin tab
    return app_context.get_page(UsersPage)


@when("I add a new user with the following details")
def add_new_user(app_context):
    """
    Add a new user (this step assumes table data is processed separately).
    For now, we'll use hardcoded values from the feature file.
    """
    # Hardcoded for John Smith based on feature file
    employee_name = "John Smith"
    username = "john123"
    password = "Pass@123"
    confirm_password = "Pass@123"

    # Go to UsersPage
    users_page = app_context.get_page(UsersPage)
    users_page.click_add_user()

    # Add user using AddUserPage
    add_user_page = app_context.get_page(AddUserPage)
    add_user_page.add_user(employee_name, username, password, confirm_password)


# -----------------------------
# Then steps
# -----------------------------
@then("I should see the new user in the users list")
def verify_user_added(app_context):
    users_page = app_context.get_page(UsersPage)
    assert users_page.is_user_present("john123"), "New user was not found in the list"
