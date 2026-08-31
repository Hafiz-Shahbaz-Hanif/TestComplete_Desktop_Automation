Feature: Add a contact
  As a user of the Contact Manager
  I want to add contacts
  So that I can keep track of people

  Background:
    Given the Contact Manager is running
    And the contact list is empty

  @smoke
  Scenario: Add a valid contact
    When I add a contact "Hafiz" "Hanif" with email "hafiz@example.com"
    Then the contact list contains "Hafiz Hanif <hafiz@example.com>"
    And the contact count is 1
    And the status message contains "Added Hafiz Hanif"

  Scenario: Reject an invalid email address
    When I add a contact "Bad" "Email" with email "not-an-email"
    Then the contact count is 0
    And the status message contains "valid email"

  Scenario: Reject a duplicate email address
    When I add a contact "Ada" "Lovelace" with email "ada@example.com"
    And I add a contact "Ada" "Byron" with email "ada@example.com"
    Then the contact count is 1
    And the status message contains "already exists"
