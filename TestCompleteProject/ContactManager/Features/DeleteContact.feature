Feature: Delete a contact
  As a user
  I want to remove contacts I no longer need

  Background:
    Given the Contact Manager is running
    And the contact list is empty

  @smoke
  Scenario: Delete the selected contact
    When I add a contact "Grace" "Hopper" with email "grace@example.com"
    And I select the contact "Grace Hopper <grace@example.com>"
    And I delete the selected contact
    Then the contact list does not contain "Grace Hopper <grace@example.com>"
    And the contact count is 0

  Scenario: Deleting without a selection is guarded
    When I delete the selected contact
    Then the status message contains "Select a contact"

  Scenario: Delete from the Edit menu
    When I add a contact "Ada" "Lovelace" with email "ada@example.com"
    And I select the contact "Ada Lovelace <ada@example.com>"
    And I delete the selected contact from the Edit menu
    Then the contact count is 0

  Scenario Outline: Delete one contact from a populated list
    Given the following contacts exist:
      | First   | Last     | Email                 |
      | Grace   | Hopper   | grace@example.com     |
      | Ada     | Lovelace | ada@example.com       |
      | Alan    | Turing   | alan@example.com      |
      | Barbara | Liskov   | barbara@example.com   |
    When I select the contact "<contact>"
    And I delete the selected contact
    Then the contact list does not contain "<contact>"
    And the contact count is 3

    Examples:
      | contact                              |
      | Grace Hopper <grace@example.com>     |
      | Ada Lovelace <ada@example.com>       |
      | Alan Turing <alan@example.com>       |
      | Barbara Liskov <barbara@example.com> |
