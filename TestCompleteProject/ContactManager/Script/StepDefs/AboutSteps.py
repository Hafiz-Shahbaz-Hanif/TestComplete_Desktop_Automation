# -*- coding: utf-8 -*-
"""Step definitions for the About dialog feature."""

from ScreenObjects.MainScreen import MainScreen
from ScreenObjects.AboutDialog import AboutDialog


# @step(r"^I open the About dialog from the Help menu$")
def open_about():
    MainScreen().menu_select("Help|About")
    AboutDialog().wait_shown()


# @step(r"^the About dialog shows version \"([^\"]*)\"$")
def about_shows_version(fragment):
    text = AboutDialog().version_text()
    if fragment.lower() not in text.lower():
        Log.Error("About version '%s' does not contain '%s'" % (text, fragment))
    else:
        Log.Checkpoint("About dialog shows version '%s'" % fragment)


# @step(r"^the About dialog shows \"([^\"]*)\"$")
def about_shows(fragment):
    text = AboutDialog().message_text() + " " + AboutDialog().version_text()
    if fragment.lower() not in text.lower():
        Log.Error("About text '%s' does not contain '%s'" % (text, fragment))
    else:
        Log.Checkpoint("About dialog shows '%s'" % fragment)


# @step(r"^I close the About dialog$")
def close_about():
    AboutDialog().close()


# @step(r"^the main window is active$")
def main_active():
    if not MainScreen().is_shown():
        Log.Error("Main window is not active after closing the dialog")
    else:
        Log.Checkpoint("Main window is active")
