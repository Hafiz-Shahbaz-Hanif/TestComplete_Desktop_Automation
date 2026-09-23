Feature: Keyboard navigation and focus
  As a keyboard-only user
  I want Tab to move focus through the form in a predictable order

  # This form sets no explicit TabIndex, so the tab order is the WinForms
  # default: Label controls are not tab stops, so only these are, in the order
  # MainForm.Designer.cs adds them via Controls.AddRange.

  Background:
    Given the Contact Manager is running
    And the contact list is empty

  @smoke
  Scenario: Tab moves focus from First name to Last name
    Given the First name field has focus
    When I press Tab 1 time
    Then the "Last name" field has focus

  Scenario Outline: Tab reaches "<control>" after <presses> presses from First name
    Given the First name field has focus
    When I press Tab <presses> times
    Then the "<control>" field has focus

    Examples:
      | control       | presses |
      | Last name     | 1       |
      | Email         | 2       |
      | Phone         | 3       |
      | Category      | 4       |
      | Favourite     | 5       |
      | Add contact   | 6       |
      | Save changes  | 7       |
      | Edit selected | 8       |
      | Clear form    | 9       |
      | Search        | 10      |
      | In category   | 11      |
