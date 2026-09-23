# -*- coding: utf-8 -*-
"""Step definitions for keyboard navigation (Tab order) on the main form.

The tab order asserted here is the real WinForms default for this SUT: Label
controls have TabStop=False by default and MainForm.Designer.cs never sets an
explicit TabIndex, so the only real tab stops are the non-Label controls, in
the order MainForm.Designer.cs adds them via Controls.AddRange - see
NameMapping.md for the full list and the source line it was read from.
"""

from ScreenObjects.MainScreen import MainScreen

_FIELD_BY_LABEL = {
    "First name": MainScreen.FIRST_NAME,
    "Last name": MainScreen.LAST_NAME,
    "Email": MainScreen.EMAIL,
    "Phone": MainScreen.PHONE,
    "Category": MainScreen.CATEGORY,
    "Favourite": MainScreen.FAVOURITE,
    "Add contact": MainScreen.ADD_BUTTON,
    "Save changes": MainScreen.SAVE_BUTTON,
    "Edit selected": MainScreen.EDIT_BUTTON,
    "Clear form": MainScreen.CLEAR_BUTTON,
    "Search": MainScreen.SEARCH,
    "In category": MainScreen.FILTER_CATEGORY,
    "Favourites only": MainScreen.FAVOURITES_ONLY,
    "Sort by": MainScreen.SORT,
}


def _main():
    return MainScreen()


# @step(r"^the First name field has focus$")
def focus_first_name():
    _main().focus(MainScreen.FIRST_NAME)


# @step(r"^I press Tab (\d+) times?$")
def press_tab(times):
    main = _main()
    for _ in range(int(times)):
        main.press_key("[Tab]")


# @step(r"^the \"([^\"]*)\" field has focus$")
def field_has_focus(label):
    name = _FIELD_BY_LABEL.get(label)
    if name is None:
        Log.Error("No known tab stop named '%s'" % label)
        return
    if _main().is_focused(name):
        Log.Checkpoint("'%s' has focus" % label)
    else:
        Log.Error("Expected '%s' to have focus" % label)
