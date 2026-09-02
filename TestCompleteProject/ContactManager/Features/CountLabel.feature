Feature: The contact count label
  As a user
  I want a live count that reflects any active filter

  Background:
    Given the Contact Manager is running
    And the contact list is empty
    And the following contacts exist:
      | First   | Last     | Email               | Category | Favourite |
      | Grace   | Hopper   | grace@example.com   | Work     | yes       |
      | Ada     | Lovelace | ada@example.com     | Work     | no        |
      | Alan    | Turing   | alan@example.com    | Friends  | yes       |
      | Barbara | Liskov   | barbara@example.com | Family   | no        |

  Scenario: No filter shows the plain total
    Then the count label shows "4 contact(s)"

  Scenario Outline: An active filter shows "<expected>"
    When <action>
    Then the count label shows "<expected>"

    Examples:
      | action                              | expected            |
      | I search for "a"                    | of 4 contact(s)     |
      | I search for "grace"                | 1 of 4 contact(s)   |
      | I filter by the "Work" category     | 2 of 4 contact(s)   |
      | I show favourites only              | 2 of 4 contact(s)   |
      | I search for "zzz"                  | 0 of 4 contact(s)   |
