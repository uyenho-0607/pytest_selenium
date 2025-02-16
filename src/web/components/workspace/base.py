from selenium.webdriver.common.by import By

from src.web.pages.base_page import BasePage


class BaseWorkspace(BasePage):
    def __init__(self, actions):
        super().__init__(actions)

    __close_btn = (By.CSS_SELECTOR, ".close-btn")

    def close(self):
        self.actions.click(self.__close_btn)
