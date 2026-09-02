Feature: Export contacts to CSV
  As a user
  I want to export my contacts through the native Save dialog

  Background:
    Given the Contact Manager is running
    And the contact list is empty

  @smoke
  Scenario: Export writes one data row per contact
    Given the following contacts exist:
      | First | Last     | Email             | Phone   | Category | Favourite |
      | Grace | Hopper   | grace@example.com | 5551234 | Work     | yes       |
      | Ada   | Lovelace | ada@example.com   |         | Friends  | no        |
    When I export the contacts to a CSV file
    Then the exported file has 2 data rows
    And the exported file header is "FirstName,LastName,Email,Phone,Category,Favourite"

  Scenario: Exported rows carry the contact details
    Given the following contacts exist:
      | First | Last   | Email             | Phone   | Category | Favourite |
      | Grace | Hopper | grace@example.com | 5551234 | Work     | yes       |
    When I export the contacts to a CSV file
    Then the exported file contains "Grace,Hopper,grace@example.com,5551234,Work,True"

  Scenario: Exporting an empty list writes only the header
    When I export the contacts to a CSV file
    Then the exported file has 0 data rows

  Scenario: Cancelling the Save dialog reports the cancellation
    When I cancel the export
    Then the status message contains "Export cancelled"
