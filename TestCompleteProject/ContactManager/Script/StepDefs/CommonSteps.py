# -*- coding: utf-8 -*-
"""Shared step definitions and assertion helpers."""

from ScreenObjects.MainScreen import MainScreen


def _main():
    return MainScreen()


# @step(r"^the Contact Manager is running$")
def app_is_running():
    # The application is launched by the scenario-start hook; this step simply
    # asserts the main window is present so the Background reads naturally.
    if not _main().is_shown():
        Log.Error("Contact Manager main window is not visible")


# @step(r"^the contact list is empty$")
def list_is_empty():
    assert_equal(_main().contact_count(), 0, "initial contact count")


# @step(r"^the following contacts exist:$")
def seed_contacts(table):
    """Data-table step. Columns: First | Last | Email | Phone | Category | Favourite.
    Only First/Last/Email are required; the rest default."""
    main = _main()
    for row in table.rows:
        main.add_contact(
            _cell(row, "First"),
            _cell(row, "Last"),
            _cell(row, "Email"),
            phone=_cell(row, "Phone") or None,
            category=_cell(row, "Category") or None,
            favourite=_truthy(_cell(row, "Favourite")),
        )


def _cell(row, name):
    try:
        value = row[name]
    except Exception:
        return ""
    return "" if value is None else str(value).strip()


# @step(r"^the contact count is (\d+)$")
def count_is(expected):
    assert_equal(_main().contact_count(), int(expected), "visible contact count")


# @step(r"^the count label shows \"([^\"]*)\"$")
def count_label_shows(fragment):
    actual = _main().displayed_count_label()
    if fragment.lower() not in actual.lower():
        Log.Error("Count label '%s' does not contain '%s'" % (actual, fragment))
    else:
        Log.Checkpoint("Count label shows '%s'" % fragment)


# @step(r"^the status message contains \"([^\"]*)\"$")
def status_contains(fragment):
    actual = _main().status_message()
    if fragment.lower() not in actual.lower():
        Log.Error("Status message '%s' does not contain '%s'" % (actual, fragment))
    else:
        Log.Checkpoint("Status message contains '%s'" % fragment)


def _truthy(value):
    return str(value).strip().lower() in ("yes", "true", "y", "1", "favourite")


def assert_equal(actual, expected, description):
    if actual == expected:
        Log.Checkpoint("%s == %s (%s)" % (actual, expected, description))
    else:
        Log.Error("Expected %s to be %s but was %s" % (description, expected, actual))
