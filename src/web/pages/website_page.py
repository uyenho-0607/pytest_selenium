
from src.web.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WebsitePage(BasePage):
    def __init__(self, elements):
        super().__init__(elements)

    username_txt = (By.ID, "login-form-username")
    password_txt = (By.ID, "txtPassword")
    signin_btn = (By.XPATH, "//button[text()='Sign In']")

    def login(self, username, password):
        self._elements.send_keys(self.username_txt, keys=username)
        self._elements.send_keys(self.password_txt, keys=password)
        self._elements.click(self.signin_btn)
