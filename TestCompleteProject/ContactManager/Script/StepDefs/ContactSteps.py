# -*- coding: utf-8 -*-
"""Step definitions for adding, listing, filtering, sorting and deleting contacts.

Each function implements one Gherkin step. TestComplete's BDD feature editor
binds a step line to the routine whose ``@step`` pattern matches it (see
``docs/BDD-INTEGRATION.md``). Steps are thin: they translate a sentence into a
Screen Object call and an assertion - no locators, no waits, no ``Sys`` here.
"""

from ScreenObjects.MainScreen import MainScreen


def _main():
    return MainScreen()


# --- adding -----------------------------------------------------------
# @step(r"^I add a contact \"([^\"]*)\" \"([^\"]*)\" with email \"([^\"]*)\"$")
def add_contact(first_name, last_name, email):
    _main().add_contact(first_name, last_name, email)


# @step(r"^I add a contact \"([^\"]*)\" \"([^\"]*)\" with email \"([^\"]*)\" and phone \"([^\"]*)\"$")
def add_contact_with_phone(first_name, last_name, email, phone):
    _main().add_contact(first_name, last_name, email, phone=phone)


# @step(r"^I add a \"([^\"]+)\" contact \"([^\"]*)\" \"([^\"]*)\" with email \"([^\"]*)\"$")
def add_categorised_contact(category, first_name, last_name, email):
    _main().add_contact(first_name, last_name, email, category=category)


# @step(r"^I add a favourite contact \"([^\"]*)\" \"([^\"]*)\" with email \"([^\"]*)\"$")
def add_favourite_contact(first_name, last_name, email):
    _main().add_contact(first_name, last_name, email, favourite=True)


# --- list assertions ----------------------------------------------
# @step(r"^the contact list contains \"([^\"]*)\"$")
def list_contains(display_text):
    if not _main().contains_contact(display_text):
        Log.Error("Expected the contact list to contain '%s'" % display_text)
    else:
        Log.Checkpoint("Contact list contains '%s'" % display_text)


# @step(r"^the contact list does not contain \"([^\"]*)\"$")
def list_excludes(display_text):
    if _main().contains_contact(display_text):
        Log.Error("Did not expect '%s' in the contact list" % display_text)
    else:
        Log.Checkpoint("Contact list does not contain '%s'" % display_text)


# @step(r"^the contacts are listed in this order:$")
def rows_in_order(table):
    expected = [row["Contact"] for row in table.rows]
    actual = _main().contact_rows_in_order()
    if actual == expected:
        Log.Checkpoint("Contacts listed in the expected order")
    else:
        Log.Error("Order mismatch.\n expected: %s\n actual:   %s" % (expected, actual))


# --- selection / deletion --------------------------------------
# @step(r"^I select the contact \"([^\"]*)\"$")
def select_contact(display_text):
    _main().select_contact(display_text)


# @step(r"^I delete the selected contact$")
def delete_selected():
    _main().delete_selected()


# @step(r"^I delete the selected contact from the Edit menu$")
def delete_via_menu():
    _main().delete_via_menu()


# --- filtering / sorting -------------------------------------
# @step(r"^I search for \"([^\"]*)\"$")
def search_for(term):
    _main().search(term)


# @step(r"^I filter by the \"([^\"]+)\" category$")
def filter_category(name):
    _main().filter_by_category(name)


# @step(r"^I show favourites only$")
def favourites_only():
    _main().show_favourites_only(True)


# @step(r"^I show contacts in every category$")
def show_all():
    main = _main()
    main.filter_by_category("All")
    main.show_favourites_only(False)


# @step(r"^I sort by \"([^\"]+)\"$")
def sort_by(key):
    _main().sort_by(key)


# --- new list -------------------------------------------------
# @step(r"^I start a new list$")
def new_list():
    _main().new_list()
