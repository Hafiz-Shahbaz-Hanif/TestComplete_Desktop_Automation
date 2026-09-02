Feature: Status bar messages
  As a user
  I want the status bar to tell me the result of every action

  Background:
    Given the Contact Manager is running
    And the contact list is empty
    And the following contacts exist:
      | First | Last     | Email             |
      | Grace | Hopper   | grace@example.com |

  Scenario Outline: The status bar reports "<message>"
    When <action>
    Then the status message contains "<message>"

    Examples:
      | action                                                          | message           |
      | I add a contact "Ada" "Lovelace" with email "ada@example.com"   | Added Ada Lovelace |
      | I add a contact "Ada" "Byron" with email "grace@example.com"    | already exists    |
      | I add a contact "" "Byron" with email "x@example.com"           | name are required |
      | I add a contact "Bad" "Email" with email "nope"                 | valid email       |
      | I delete the selected contact                                   | Select a contact  |
      | I start a new list                                              | new contact list  |
      | I clear the form                                                | Form cleared      |
      | I cancel the export                                             | Export cancelled  |

  Scenario: Selecting then deleting reports the deleted name
    When I select the contact "Grace Hopper <grace@example.com>"
    And I delete the selected contact
    Then the status message contains "Deleted Grace Hopper"
