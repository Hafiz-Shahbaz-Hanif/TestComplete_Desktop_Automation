Feature: Phone number handling
  As a user
  I want phone numbers to be optional but well-formed when present

  Background:
    Given the Contact Manager is running
    And the contact list is empty

  Scenario Outline: Accept well-formed phone numbers
    When I add a contact "Pat" "Ng" with email "<email>" and phone "<phone>"
    Then the contact count is 1
    And the status message contains "Added Pat Ng"

    Examples:
      | email            | phone            |
      | p1@example.com   |                  |
      | p2@example.com   | 5551234          |
      | p3@example.com   | 555 123 4567     |
      | p4@example.com   | +1 (555) 123-456 |
      | p5@example.com   | +92-300-1234567  |
      | p6@example.com   | (021) 111 222    |

  Scenario Outline: Reject malformed phone numbers
    When I add a contact "Pat" "Ng" with email "<email>" and phone "<phone>"
    Then the contact count is 0
    And the status message contains "valid phone"

    Examples:
      | email            | phone       |
      | q1@example.com   | 123         |
      | q2@example.com   | abcdefg     |
      | q3@example.com   | 555-CALL    |
      | q4@example.com   | 12 34       |
      | q5@example.com   | ++++++      |
      | q6@example.com   | 555.12      |
