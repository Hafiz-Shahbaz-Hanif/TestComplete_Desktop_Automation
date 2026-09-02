# -*- coding: utf-8 -*-
"""MainScreen - the Contact Manager main window."""

from ScreenObjects.BaseScreen import BaseScreen
from ScreenObjects.ExportDialog import ExportDialog
from Support import Waits


class MainScreen(BaseScreen):
    ROOT_ALIAS = "MainForm"

    # NameMapping ids for this screen's controls.
    FIRST_NAME = "txtFirstName"
    LAST_NAME = "txtLastName"
    EMAIL = "txtEmail"
    PHONE = "txtPhone"
    CATEGORY = "cboCategory"
    FAVOURITE = "chkFavourite"
    ADD_BUTTON = "btnAdd"
    SAVE_BUTTON = "btnSave"
    EDIT_BUTTON = "btnEdit"
    CLEAR_BUTTON = "btnClear"
    SEARCH = "txtSearch"
    FILTER_CATEGORY = "cboFilterCategory"
    FAVOURITES_ONLY = "chkFavouritesOnly"
    SORT = "cboSort"
    LIST = "lstContacts"
    DELETE_BUTTON = "btnDelete"
    COUNT_LABEL = "lblCount"

    # --- form actions --------------------------------------------------
    def fill_form(self, first_name, last_name, email,
                  phone=None, category=None, favourite=None):
        self.set_text(self.FIRST_NAME, first_name)
        self.set_text(self.LAST_NAME, last_name)
        self.set_text(self.EMAIL, email)
        if phone is not None:
            self.set_text(self.PHONE, phone)
        if category is not None:
            self.select_combo(self.CATEGORY, category)
        if favourite is not None:
            self.set_checkbox(self.FAVOURITE, favourite)
        return self

    def add_contact(self, first_name, last_name, email,
                    phone=None, category=None, favourite=None):
        self.fill_form(first_name, last_name, email, phone, category, favourite)
        self.click(self.ADD_BUTTON)
        return self

    def start_editing(self):
        self.click(self.EDIT_BUTTON)
        return self

    def save_changes(self):
        self.click(self.SAVE_BUTTON)
        return self

    def clear_form(self):
        self.click(self.CLEAR_BUTTON)
        return self

    def save_button_enabled(self):
        return self.is_enabled(self.SAVE_BUTTON)

    # --- list actions ------------------------------------------------
    def search(self, term):
        self.set_text(self.SEARCH, term)
        Waits.for_ui_idle()
        return self

    def filter_by_category(self, name):
        self.select_combo(self.FILTER_CATEGORY, name)
        Waits.for_ui_idle()
        return self

    def show_favourites_only(self, on=True):
        self.set_checkbox(self.FAVOURITES_ONLY, on)
        Waits.for_ui_idle()
        return self

    def sort_by(self, key):
        self.select_combo(self.SORT, key)
        Waits.for_ui_idle()
        return self

    def select_contact(self, display_text):
        self.control(self.LIST).ClickItem(display_text)
        return self

    def delete_selected(self):
        self.click(self.DELETE_BUTTON)
        return self

    # --- menu actions ----------------------------------------------
    def new_list(self):
        self.menu_select("File|New list")
        return self

    def edit_via_menu(self):
        self.menu_select("Edit|Edit selected")
        return self

    def delete_via_menu(self):
        self.menu_select("Edit|Delete selected")
        return self

    def export(self):
        """Open File -> Export to CSV... and return the native Save dialog screen."""
        self.menu_select("File|Export to CSV...")
        return ExportDialog().wait_shown()

    def exit_via_menu(self):
        self.menu_select("File|Exit")

    # --- queries -------------------------------------------------------
    def visible_contacts(self):
        items = self.control(self.LIST).Items
        return [items.Item[i].OleValue for i in range(items.Count)]

    def contact_count(self):
        return len(self.visible_contacts())

    def contact_rows_in_order(self):
        return list(self.visible_contacts())

    def displayed_count_label(self):
        return self.get_text(self.COUNT_LABEL)

    def status_message(self):
        return self.root.statusStrip.Panels.Item[0].Text

    def contains_contact(self, display_text):
        return any(display_text in row for row in self.visible_contacts())

    def form_first_name(self):
        return self.get_text(self.FIRST_NAME)
