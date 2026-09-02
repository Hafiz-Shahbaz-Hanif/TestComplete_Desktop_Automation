# -*- coding: utf-8 -*-
"""AboutDialog - the modal Help -> About window.

A second screen object, included to show how the SOM handles modal dialogs:
the screen is resolved as a child of the process (not of MainForm) and
``wait_shown`` waits for the modal window to appear.
"""

from ScreenObjects.BaseScreen import BaseScreen


class AboutDialog(BaseScreen):
    ROOT_ALIAS = "AboutForm"

    VERSION = "lblVersion"
    MESSAGE = "lblAbout"
    OK_BUTTON = "btnAboutOk"

    def version_text(self):
        return self.get_text(self.VERSION)

    def message_text(self):
        return self.get_text(self.MESSAGE)

    def close(self):
        self.click(self.OK_BUTTON)
