Feature: Search the contact list
  As a user with many contacts
  I want to filter the list
  So that I can find a person quickly

  Background:
    Given the Contact Manager is running
    And the contact list is empty

  Scenario: Filter narrows the list to matches
    When I add a contact "Hafiz" "Hanif" with email "hafiz@example.com"
    And I add a contact "Grace" "Hopper" with email "grace@example.com"
    And I search for "hop"
    Then the contact list contains "Grace Hopper <grace@example.com>"
    And the contact list does not contain "Hafiz Hanif <hafiz@example.com>"
    And the contact count is 1

  Scenario: Clearing the filter restores the full list
    When I add a contact "Hafiz" "Hanif" with email "hafiz@example.com"
    And I add a contact "Grace" "Hopper" with email "grace@example.com"
    And I search for "hop"
    And I search for ""
    Then the contact count is 2
