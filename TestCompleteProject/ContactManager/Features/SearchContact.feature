Feature: Search the contact list
  As a user with many contacts
  I want to filter the list as I type
  So that I can find a person quickly

  Background:
    Given the Contact Manager is running
    And the contact list is empty
    And the following contacts exist:
      | First   | Last     | Email                 | Phone        |
      | Grace   | Hopper   | grace@example.com     | 5551000      |
      | Ada     | Lovelace | ada@navy.example.com  | 5552000      |
      | Alan    | Turing   | alan@example.com      | 5553000      |
      | Barbara | Liskov   | barbara@example.com   | 5551234      |
      | Katie   | Bouman   | katie@example.com     | 5559999      |

  @smoke
  Scenario: Filter narrows the list to matches
    When I search for "hop"
    Then the contact list contains "Grace Hopper <grace@example.com>"
    And the contact list does not contain "Alan Turing <alan@example.com>"
    And the contact count is 1

  Scenario: Clearing the filter restores the full list
    When I search for "hop"
    And I search for ""
    Then the contact count is 5

  Scenario Outline: Search term matches name, email or phone
    When I search for "<term>"
    Then the contact count is <count>

    Examples:
      | term        | count |
      | hopper      | 1     |
      | grace       | 1     |
      | turing      | 1     |
      | navy        | 1     |
      | 5551234     | 1     |
      | example.com | 5     |
      | LISKOV      | 1     |
      | zzz         | 0     |
      | @example    | 5     |
      | bouman      | 1     |
