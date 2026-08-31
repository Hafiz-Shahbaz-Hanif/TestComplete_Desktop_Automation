Feature: Delete a contact
  As a user of the Contact Manager
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
