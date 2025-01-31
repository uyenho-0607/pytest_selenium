from selenium.webdriver.common.by import By
from src.web.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, element=None):
        super().__init__(element)

    tab_bar = (By.ID, "tab-barr")

    def verify_login_success(self):
        self._elements.verify_is_displayed(self.tab_bar)

