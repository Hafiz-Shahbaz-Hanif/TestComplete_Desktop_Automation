# -*- coding: utf-8 -*-
"""Step definitions for the Contact Manager features.

Each function implements one Gherkin step. TestComplete's BDD feature editor
binds a step line to the routine whose ``@step`` pattern matches it (see
``docs/BDD-INTEGRATION.md``). Steps are thin: they translate a sentence into a
Screen Object call and an assertion - no locators, no waits, no ``Sys`` here.
"""

from ScreenObjects.MainScreen import MainScreen
from StepDefs import CommonSteps


def _main():
    return MainScreen()


# @step(r"I add a contact \"(.+)\" \"(.+)\" with email \"(.+)\"")
def add_contact(first_name, last_name, email):
    _main().add_contact(first_name, last_name, email)


# @step(r"the contact list contains \"(.+)\"")
def list_contains(display_text):
    if not _main().contains_contact(display_text):
        Log.Error("Expected the contact list to contain '%s'" % display_text)
    else:
        Log.Checkpoint("Contact list contains '%s'" % display_text)


# @step(r"the contact list does not contain \"(.+)\"")
def list_excludes(display_text):
    if _main().contains_contact(display_text):
        Log.Error("Did not expect '%s' in the contact list" % display_text)
    else:
        Log.Checkpoint("Contact list does not contain '%s'" % display_text)


# @step(r"the contact count is (\d+)")
def count_is(expected):
    CommonSteps.assert_equal(_main().contact_count(), int(expected), "visible contact count")


# @step(r"the status message contains \"(.+)\"")
def status_contains(fragment):
    actual = _main().status_message()
    if fragment.lower() not in actual.lower():
        Log.Error("Status message '%s' does not contain '%s'" % (actual, fragment))
    else:
        Log.Checkpoint("Status message contains '%s'" % fragment)


# @step(r"I select the contact \"(.+)\"")
def select_contact(display_text):
    _main().select_contact(display_text)


# @step(r"I delete the selected contact")
def delete_selected():
    _main().delete_selected()


# @step(r"I search for \"(.*)\"")
def search_for(term):
    _main().search(term)
