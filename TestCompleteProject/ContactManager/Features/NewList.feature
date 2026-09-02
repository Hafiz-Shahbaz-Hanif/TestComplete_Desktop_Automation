Feature: Start a new list
  As a user
  I want File > New list to clear everything

  Background:
    Given the Contact Manager is running
    And the contact list is empty
    And the following contacts exist:
      | First | Last     | Email             |
      | Grace | Hopper   | grace@example.com |
      | Ada   | Lovelace | ada@example.com   |

  @smoke
  Scenario: New list empties the contact list
    When I start a new list
    Then the contact count is 0
    And the status message contains "new contact list"

  Scenario: New list clears an in-progress edit
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    And I start a new list
    Then the Save button is disabled

  Scenario: Contacts can be added again after New list
    When I start a new list
    And I add a contact "Alan" "Turing" with email "alan@example.com"
    Then the contact count is 1
