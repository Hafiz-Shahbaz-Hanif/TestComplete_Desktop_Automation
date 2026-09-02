# -*- coding: utf-8 -*-
"""ExportDialog - the native Windows "Export contacts" Save dialog.

A third screen object, included to show that a **native OS dialog** (window class
``#32770``) is modelled exactly like an in-app screen: mapped by window class,
driven through the same primitives, waited on with the same explicit waits.
"""

from ScreenObjects.BaseScreen import BaseScreen


class ExportDialog(BaseScreen):
    ROOT_ALIAS = "ExportDialog"

    FILE_NAME = "FileName"
    SAVE_BUTTON = "SaveButton"

    def save_as(self, path):
        self.set_text(self.FILE_NAME, path)
        self.click(self.SAVE_BUTTON)

    def cancel(self):
        self.root.Keys("[Esc]")
