# -*- coding: utf-8 -*-
"""Step definitions for editing an existing contact."""

from ScreenObjects.MainScreen import MainScreen


_FIELD_IDS = {
    "first name": MainScreen.FIRST_NAME,
    "last name": MainScreen.LAST_NAME,
    "email": MainScreen.EMAIL,
    "phone": MainScreen.PHONE,
}


def _main():
    return MainScreen()


# @step(r"^I edit the selected contact$")
def start_editing():
    _main().start_editing()


# @step(r"^I edit the selected contact from the Edit menu$")
def start_editing_via_menu():
    _main().edit_via_menu()


# @step(r"^I change the (first name|last name|email|phone) to \"([^\"]*)\"$")
def change_field(field, value):
    _main().set_text(_FIELD_IDS[field], value)


# @step(r"^I change the category to \"([^\"]+)\"$")
def change_category(value):
    _main().select_combo(MainScreen.CATEGORY, value)


# @step(r"^I mark the contact as favourite$")
def mark_favourite():
    _main().set_checkbox(MainScreen.FAVOURITE, True)


# @step(r"^I unmark the contact as favourite$")
def unmark_favourite():
    _main().set_checkbox(MainScreen.FAVOURITE, False)


# @step(r"^I save the changes$")
def save_changes():
    _main().save_changes()


# @step(r"^I clear the form$")
def clear_form():
    _main().clear_form()


# @step(r"^the first name field shows \"([^\"]*)\"$")
def first_name_field_shows(value):
    actual = _main().form_first_name()
    if actual == value:
        Log.Checkpoint("First name field shows '%s'" % value)
    else:
        Log.Error("First name field shows '%s', expected '%s'" % (actual, value))


# @step(r"^the Save button is (enabled|disabled)$")
def save_button_state(state):
    enabled = _main().save_button_enabled()
    expected = state == "enabled"
    if enabled == expected:
        Log.Checkpoint("Save button is %s" % state)
    else:
        Log.Error("Save button enabled=%s, expected %s" % (enabled, state))
