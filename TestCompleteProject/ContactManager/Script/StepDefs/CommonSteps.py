# -*- coding: utf-8 -*-
"""Shared step definitions and assertion helpers."""

from ScreenObjects.MainScreen import MainScreen


# @step(r"the Contact Manager is running")
def app_is_running():
    # The application is launched by the scenario-start hook; this step simply
    # asserts the main window is present so the Background reads naturally.
    if not MainScreen().is_shown():
        Log.Error("Contact Manager main window is not visible")


# @step(r"the contact list is empty")
def list_is_empty():
    assert_equal(MainScreen().contact_count(), 0, "initial contact count")


def assert_equal(actual, expected, description):
    if actual == expected:
        Log.Checkpoint("%s == %s (%s)" % (actual, expected, description))
    else:
        Log.Error("Expected %s to be %s but was %s" % (description, expected, actual))
