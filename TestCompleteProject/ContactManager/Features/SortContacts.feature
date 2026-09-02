Feature: Sort the contact list
  As a user
  I want to reorder the list by name, email or category

  Background:
    Given the Contact Manager is running
    And the contact list is empty
    And the following contacts exist:
      | First   | Last     | Email               | Category |
      | Grace   | Hopper   | zeta@example.com    | Work     |
      | Ada     | Lovelace | alpha@example.com   | Friends  |
      | Barbara | Liskov   | mu@example.com      | Family   |

  Scenario: Sort by name
    When I sort by "Name"
    Then the contacts are listed in this order:
      | Contact                              |
      | Ada Lovelace <alpha@example.com>     |
      | Barbara Liskov <mu@example.com>      |
      | Grace Hopper <zeta@example.com>      |

  Scenario: Sort by email
    When I sort by "Email"
    Then the contacts are listed in this order:
      | Contact                              |
      | Ada Lovelace <alpha@example.com>     |
      | Barbara Liskov <mu@example.com>      |
      | Grace Hopper <zeta@example.com>      |

  Scenario: Sort by category
    When I sort by "Category"
    Then the contacts are listed in this order:
      | Contact                              |
      | Barbara Liskov <mu@example.com>      |
      | Ada Lovelace <alpha@example.com>     |
      | Grace Hopper <zeta@example.com>      |

  Scenario Outline: The chosen sort survives a filter change
    When I sort by "<key>"
    And I search for "e"
    And I search for ""
    Then the contact count is 3

    Examples:
      | key      |
      | Name     |
      | Email    |
      | Category |
