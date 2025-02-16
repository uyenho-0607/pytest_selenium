
from src.web.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, actions):
        super().__init__(actions)

    username_txt = (By.ID, "login-form-username")
    password_txt = (By.ID, "txtPassword")
    signin_btn = (By.XPATH, "//button[text()='Sign In']")

    def login(self, username, password):
        self.actions.send_keys(self.username_txt, keys=username)
        self.actions.send_keys_and_press_enter(self.password_txt, keys=password)
