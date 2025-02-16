from selenium.webdriver.common.by import By

from src.data.enums import Collections
from src.web.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, actions):
        super().__init__(actions)

    __tab_bar = (By.ID, "tab-bar")
    __custom_view_tab = (By.CSS_SELECTOR, ".custom-view-tabs ul.system-nav li")
    __collection_info = (By.CSS_SELECTOR, "ul.system-nav li.icollection-info")

    def verify_login_succeeded(self):
        self.actions.verify_is_displayed(self.__tab_bar)

    def __toggle_page(self, page_name, open_page=True):
        options = self.actions.safe_find_elements(self.__custom_view_tab)
        for option in options:
            if option.get_attribute("analytics-event") == page_name:
                is_open = option.get_attribute("analytics-open") == "true"
                if (open_page and is_open) or (not open_page and not is_open):
                    option.click()
                    return

    def toggle_collection_picker(self, open_page=True):
        is_open = self.actions.get_attribute(self.__collection_info, "analytics-open")
        if (open_page and is_open) or (not open_page and not is_open):
            self.actions.click(self.__collection_info)

    def toggle_channels_page(self, open_page=True):
        self.__toggle_page(Collections.SmartCollections.CHANNELS, open_page)

    def toggle_todos_page(self, open_page=True):
        self.__toggle_page(Collections.SmartCollections.TODOS, open_page)

    def toggle_note_page(self, open_page=True):
        self.__toggle_page(Collections.SmartCollections.NOTES, open_page)
