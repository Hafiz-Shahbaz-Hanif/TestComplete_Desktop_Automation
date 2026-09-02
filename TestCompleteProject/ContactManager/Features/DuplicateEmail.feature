Feature: Duplicate email addresses
  As a user
  I want the app to treat email as the unique key
  So that I never store the same person twice

  Background:
    Given the Contact Manager is running
    And the contact list is empty

  @smoke
  Scenario: Reject a second contact with the same email
    When I add a contact "Ada" "Lovelace" with email "ada@example.com"
    And I add a contact "Ada" "Byron" with email "ada@example.com"
    Then the contact count is 1
    And the status message contains "already exists"

  Scenario Outline: Email match is case-insensitive
    Given the following contacts exist:
      | First | Last     | Email             |
      | Ada   | Lovelace | ada@example.com   |
    When I add a contact "Ada" "Clone" with email "<email>"
    Then the contact count is 1
    And the status message contains "already exists"

    Examples:
      | email             |
      | ada@example.com   |
      | ADA@example.com   |
      | Ada@Example.Com   |
      | ada@EXAMPLE.com   |
