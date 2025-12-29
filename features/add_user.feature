Feature: Add new user in OrangeHRM

  Scenario: Admin can add a new user
    Given I am on the login page
    When I login with valid credentials
    And I navigate to the Users page
    And I add a new user with the following details
    Then I should see the new user in the users list
