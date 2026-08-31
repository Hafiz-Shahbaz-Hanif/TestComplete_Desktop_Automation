# -*- coding: utf-8 -*-
"""MainScreen - the Contact Manager main window."""

from ScreenObjects.BaseScreen import BaseScreen
from Support import Waits


class MainScreen(BaseScreen):
    ROOT_ALIAS = "MainForm"

    # NameMapping ids for this screen's controls.
    FIRST_NAME = "txtFirstName"
    LAST_NAME = "txtLastName"
    EMAIL = "txtEmail"
    ADD_BUTTON = "btnAdd"
    SEARCH = "txtSearch"
    LIST = "lstContacts"
    DELETE_BUTTON = "btnDelete"
    COUNT_LABEL = "lblCount"
    STATUS_LABEL = "statusStrip"

    # --- actions --------------------------------------------------------
    def add_contact(self, first_name, last_name, email):
        self.set_text(self.FIRST_NAME, first_name)
        self.set_text(self.LAST_NAME, last_name)
        self.set_text(self.EMAIL, email)
        self.click(self.ADD_BUTTON)
        return self

    def search(self, term):
        self.set_text(self.SEARCH, term)
        Waits.for_ui_idle()
        return self

    def select_contact(self, display_text):
        self.control(self.LIST).ClickItem(display_text)
        return self

    def delete_selected(self):
        self.click(self.DELETE_BUTTON)
        return self

    def exit_via_menu(self):
        self.menu_select("File|Exit")

    # --- queries -------------------------------------------------------
    def visible_contacts(self):
        items = self.control(self.LIST).Items
        return [items.Item[i].OleValue for i in range(items.Count)]

    def contact_count(self):
        return len(self.visible_contacts())

    def displayed_count_label(self):
        return self.get_text(self.COUNT_LABEL)

    def status_message(self):
        return self.root.statusStrip.Panels.Item[0].Text

    def contains_contact(self, display_text):
        return any(display_text in row for row in self.visible_contacts())
