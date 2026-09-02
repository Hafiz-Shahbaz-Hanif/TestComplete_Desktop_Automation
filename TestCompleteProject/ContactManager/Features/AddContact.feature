Feature: Add a contact
  As a user of the Contact Manager
  I want to add contacts with their details
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

  Scenario: The entry form clears after a successful add
    When I add a contact "Grace" "Hopper" with email "grace@example.com"
    Then the first name field shows ""

  Scenario Outline: Add a contact in every category
    When I add a "<category>" contact "<first>" "<last>" with email "<email>"
    Then the contact list contains "<first> <last> <<email>>"
    And the contact count is 1
    And the status message contains "Added <first> <last>"

    Examples:
      | category | first   | last      | email                   |
      | Family   | Ada     | Lovelace  | ada@example.com         |
      | Family   | Charles | Babbage   | charles@example.com     |
      | Friends  | Alan    | Turing    | alan@example.com        |
      | Friends  | Edsger  | Dijkstra  | edsger@example.com      |
      | Work     | Barbara | Liskov    | barbara@example.com     |
      | Work     | Donald  | Knuth     | donald@example.com      |
      | Work     | Margaret| Hamilton  | margaret@example.com    |
      | Other    | Katherine| Johnson  | katherine@example.com   |
      | Other    | Dennis  | Ritchie   | dennis@example.com      |
      | Other    | Ken     | Thompson  | ken@example.com         |
      | Friends  | Radia   | Perlman   | radia@example.com       |
      | Family   | Hedy    | Lamarr    | hedy@example.com        |

  Scenario Outline: Add a contact with a phone number and favourite flag
    When I add a favourite contact "<first>" "<last>" with email "<email>"
    Then the contact list contains "<first> <last> <<email>>"
    And the status message contains "Added <first> <last>"

    Examples:
      | first    | last     | email                |
      | Grace    | Hopper   | grace2@example.com   |
      | Adele    | Goldberg | adele@example.com    |
      | Frances  | Allen    | frances@example.com  |
      | Jean     | Bartik   | jean@example.com     |
      | Evelyn   | Granville| evelyn@example.com   |
      | Annie    | Easley   | annie@example.com    |
