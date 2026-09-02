Feature: Filter by category and favourites
  As a user
  I want to narrow the list by category or to favourites only

  Background:
    Given the Contact Manager is running
    And the contact list is empty
    And the following contacts exist:
      | First   | Last     | Email                 | Category | Favourite |
      | Grace   | Hopper   | grace@example.com     | Work     | yes       |
      | Ada     | Lovelace | ada@example.com       | Work     | no        |
      | Alan    | Turing   | alan@example.com      | Friends  | yes       |
      | Barbara | Liskov   | barbara@example.com   | Family   | no        |
      | Katie   | Bouman   | katie@example.com     | Other    | no        |

  Scenario Outline: Filter to a single category
    When I filter by the "<category>" category
    Then the contact count is <count>
    And the count label shows "of 5"

    Examples:
      | category | count |
      | Work     | 2     |
      | Friends  | 1     |
      | Family   | 1     |
      | Other    | 1     |

  Scenario: Filtering back to All restores the list
    When I filter by the "Work" category
    And I filter by the "All" category
    Then the contact count is 5
    And the count label shows "5 contact(s)"

  Scenario: Favourites only
    When I show favourites only
    Then the contact count is 2
    And the contact list contains "★ Grace Hopper <grace@example.com>"
    And the contact list contains "★ Alan Turing <alan@example.com>"

  Scenario: Category and favourites combine
    When I filter by the "Work" category
    And I show favourites only
    Then the contact count is 1
    And the contact list contains "★ Grace Hopper <grace@example.com>"

  Scenario: Reset both filters
    When I filter by the "Family" category
    And I show favourites only
    And I show contacts in every category
    Then the contact count is 5
