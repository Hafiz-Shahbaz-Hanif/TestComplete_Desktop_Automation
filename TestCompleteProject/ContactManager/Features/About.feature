Feature: About dialog
  As a user
  I want an About dialog
  So that I can see the application version

  Background:
    Given the Contact Manager is running

  @smoke
  Scenario: Open and close the About dialog
    When I open the About dialog from the Help menu
    Then the About dialog shows version "2.0"
    When I close the About dialog
    Then the main window is active

  Scenario: The About dialog names the showcase
    When I open the About dialog from the Help menu
    Then the About dialog shows "TestComplete automation showcase"

  Scenario: The About dialog states there is no proprietary code
    When I open the About dialog from the Help menu
    Then the About dialog shows "No proprietary code"
