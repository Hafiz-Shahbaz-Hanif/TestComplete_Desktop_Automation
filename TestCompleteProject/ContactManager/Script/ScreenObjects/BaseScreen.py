# -*- coding: utf-8 -*-
"""BaseScreen - the root of the Screen Object Model.

Every screen class inherits from :class:`BaseScreen`, which centralises:

* resolving the screen's root window through project Aliases
* explicit, timeout-driven waits (no fixed Delay() calls in screen code)
* the small set of interaction primitives the screens are allowed to use

Step definitions call intent-revealing screen methods only; they never touch
Aliases, NameMapping paths or ``Sys`` directly.
"""

from Support import Config
from Support import Waits


class BaseScreen(object):
    # Alias-relative path to the screen's root object, e.g. "MainForm".
    # Subclasses override this.
    ROOT_ALIAS = None

    def __init__(self):
        if self.ROOT_ALIAS is None:
            raise Exception("Screen '%s' must set ROOT_ALIAS" % type(self).__name__)
        self._app_alias = Aliases.ContactManager

    # --- object resolution -------------------------------------------------
    @property
    def root(self):
        """The screen's root window, resolved lazily each call so a re-shown
        window is picked up without recreating the screen object."""
        return getattr(self._app_alias, self.ROOT_ALIAS)

    def control(self, name):
        """Return a mapped child control of this screen by its NameMapping id."""
        return getattr(self.root, name)

    # --- lifecycle -------------------------------------------------------
    def wait_shown(self, timeout_ms=None):
        Waits.until_visible(self.root, timeout_ms or Config.WAIT_TIMEOUT_MS)
        return self

    def is_shown(self):
        return self.root.Exists and self.root.VisibleOnScreen

    # --- primitives (the only Win32 interactions screens may use) --------
    def click(self, name):
        control = self.control(name)
        Waits.until_enabled(control, Config.WAIT_TIMEOUT_MS)
        control.ClickButton() if _is_button(control) else control.Click()

    def set_text(self, name, value):
        field = self.control(name)
        Waits.until_enabled(field, Config.WAIT_TIMEOUT_MS)
        field.SetText(value)

    def get_text(self, name):
        return self.control(name).wText

    def is_enabled(self, name):
        return self.control(name).Enabled

    def select_combo(self, name, value):
        combo = self.control(name)
        Waits.until_enabled(combo, Config.WAIT_TIMEOUT_MS)
        combo.ClickItem(value)

    def combo_value(self, name):
        return self.control(name).wText

    def set_checkbox(self, name, checked):
        box = self.control(name)
        Waits.until_enabled(box, Config.WAIT_TIMEOUT_MS)
        if bool(box.wChecked) != bool(checked):
            box.ClickButton()

    def checkbox_checked(self, name):
        return bool(self.control(name).wChecked)

    def menu_select(self, path):
        """Select a menu item by its caption path, e.g. 'File|Exit'."""
        self.root.MainMenu.Click(path)


def _is_button(control):
    try:
        return aqObject.IsSupported(control, "ClickButton")
    except Exception:
        return False
