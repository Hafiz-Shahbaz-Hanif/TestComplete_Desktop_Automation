Feature: Add-contact validation
  As a user
  I want the form to reject bad input
  So that the contact list stays clean

  Background:
    Given the Contact Manager is running
    And the contact list is empty

  Scenario Outline: Reject invalid input
    When I add a contact "<first>" "<last>" with email "<email>" and phone "<phone>"
    Then the contact count is 0
    And the status message contains "<message>"

    Examples:
      | first | last   | email                | phone      | message           |
      |       | Hanif  | hafiz@example.com    |            | name are required |
      | Hafiz |        | hafiz@example.com    |            | name are required |
      |       |        | hafiz@example.com    |            | name are required |
      | Hafiz | Hanif  | not-an-email         |            | valid email       |
      | Hafiz | Hanif  | missing-at.example   |            | valid email       |
      | Hafiz | Hanif  | spaces in@email.com  |            | valid email       |
      | Hafiz | Hanif  | trailing@dot.        |            | valid email       |
      | Hafiz | Hanif  | @nodomain.com        |            | valid email       |
      | Hafiz | Hanif  |                      |            | valid email       |
      | Hafiz | Hanif  | ok@example.com       | abc        | valid phone       |
      | Hafiz | Hanif  | ok@example.com       | 123        | valid phone       |
      | Hafiz | Hanif  | ok@example.com       | 12-34      | valid phone       |
      | Hafiz | Hanif  | ok@example.com       | phone!!    | valid phone       |
      | Hafiz | Hanif  | ok@example.com       | 000 000 x  | valid phone       |
