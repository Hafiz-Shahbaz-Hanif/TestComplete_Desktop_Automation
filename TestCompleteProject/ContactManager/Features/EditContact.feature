Feature: Edit a contact
  As a user
  I want to correct a contact's details
  So that the list stays accurate

  Background:
    Given the Contact Manager is running
    And the contact list is empty
    And the following contacts exist:
      | First | Last   | Email             | Phone     | Category | Favourite |
      | Grace | Hopper | grace@example.com | 5551234   | Work     | no        |

  @smoke
  Scenario: Save button is disabled until a contact is being edited
    Then the Save button is disabled
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    Then the Save button is enabled

  Scenario: Editing loads the contact into the form
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    Then the first name field shows "Grace"

  Scenario Outline: Change one field and save
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    And I change the <field> to "<value>"
    And I save the changes
    Then the contact list contains "<expected>"
    And the status message contains "Updated"
    And the contact count is 1

    Examples:
      | field      | value               | expected                          |
      | first name | Grace B.            | Grace B. Hopper <grace@example.com> |
      | last name  | Hopper-Murray       | Grace Hopper-Murray <grace@example.com> |
      | email      | ghopper@example.com | Grace Hopper <ghopper@example.com> |
      | phone      | 555 9999            | Grace Hopper <grace@example.com>   |

  Scenario: Marking a contact as favourite while editing
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    And I mark the contact as favourite
    And I save the changes
    Then the contact list contains "★ Grace Hopper <grace@example.com>"

  Scenario: Un-favouriting a contact while editing
    Given the following contacts exist:
      | First | Last   | Email             | Category | Favourite |
      | Ada   | Lovelace | ada@example.com | Friends  | yes       |
    When I select the contact "★ Ada Lovelace <ada@example.com>"
    And I edit the selected contact
    And I unmark the contact as favourite
    And I save the changes
    Then the contact list contains "Ada Lovelace <ada@example.com>"
    And the contact list does not contain "★ Ada Lovelace <ada@example.com>"

  Scenario: Changing a contact's category while editing
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    And I change the category to "Friends"
    And I save the changes
    And I filter by the "Friends" category
    Then the contact list contains "Grace Hopper <grace@example.com>"

  Scenario: Clearing the form abandons the edit
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact
    And I change the first name to "Wrong"
    And I clear the form
    Then the Save button is disabled
    And the contact list contains "Grace Hopper <grace@example.com>"

  Scenario: Edit the selected contact from the Edit menu
    When I select the contact "Grace Hopper <grace@example.com>"
    And I edit the selected contact from the Edit menu
    Then the Save button is enabled
