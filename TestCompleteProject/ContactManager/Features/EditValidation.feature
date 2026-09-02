Feature: Edit-contact validation
  As a user
  I want edits to be validated just like new contacts

  Background:
    Given the Contact Manager is running
    And the contact list is empty
    And the following contacts exist:
      | First | Last     | Email               |
      | Grace | Hopper   | grace@example.com   |
      | Ada   | Lovelace | ada@example.com     |

  Scenario Outline: Reject an invalid edit
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    And I change the <field> to "<value>"
    And I save the changes
    Then the status message contains "<message>"
    And the contact list contains "Grace Hopper <grace@example.com>"

    Examples:
      | field      | value          | message           |
      | first name |                | name are required |
      | last name  |                | name are required |
      | email      | not-an-email   | valid email       |
      | email      |                | valid email       |
      | phone      | 12             | valid phone       |
      | phone      | letters        | valid phone       |

  Scenario: Reject an edit that collides with another contact's email
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    And I change the email to "ada@example.com"
    And I save the changes
    Then the status message contains "already exists"
    And the contact count is 2

  Scenario: Keeping the same email while editing is allowed
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    And I change the first name to "Gráinne"
    And I save the changes
    Then the contact list contains "Gráinne Hopper <grace@example.com>"
