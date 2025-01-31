from selenium.webdriver.common.by import By

from src.data.enum import Collections
from src.utils.common_util import cook_element
from src.web.pages.base_page import BasePage


class TopNavigation(BasePage):
    def __init__(self, elements):
        super().__init__(elements)

    _collections_icon = (By.CSS_SELECTOR, '.icollection-info')
    # icon for todo, notes, contacts, channels, calendar, email
    _tooltip_icon = (By.XPATH, '//tooltip//a[@tooltip-template="{}"]')
    _settings_icon = (By.CSS_SELECTOR, ".setting-item")

    def open_collection_picker(self):
        is_closed = "is-open" not in self._elements.get_attribute(self._collections_icon, "class")
        if is_closed:
            self._elements.click(self._collections_icon)

    def __open_system_collection(self, system_col=""):

        ele = cook_element(self._tooltip_icon, system_col)
        is_closed = "active" not in self._elements.get_attribute(ele, "class")
        if is_closed:
            self._elements.click(ele)

    def open_todos_page(self):
        self.__open_system_collection(Collections.SmartCollections.TODOS)

    def open_notes_page(self):
        self.__open_system_collection(Collections.SmartCollections.NOTES)

    def open_channels_page(self):
        self.__open_system_collection(Collections.SmartCollections.CHANNELS)

    def open_calendar_page(self):
        self.__open_system_collection(Collections.SmartCollections.CALENDAR)

    def open_email_page(self):
        self.__open_system_collection(Collections.SmartCollections.EMAIL)

    def open_contact_page(self):
        self.__open_system_collection(Collections.SmartCollections.CONTACTS)

    def open_settings_page(self):
        is_closed = "active" not in self._elements.get_attribute(self._settings_icon, "class")
        if is_closed:
            self._elements.click(self._settings_icon)

