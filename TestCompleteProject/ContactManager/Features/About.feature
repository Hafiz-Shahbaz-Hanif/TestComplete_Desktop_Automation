Feature: About dialog
  As a user
  I want an About dialog
  So that I can see the application version

  Background:
    Given the Contact Manager is running

  @smoke
  Scenario: Open and close the About dialog
    When I open the About dialog from the Help menu
    Then the About dialog shows "Contact Manager 1.0"
    When I close the About dialog
    Then the main window is active
