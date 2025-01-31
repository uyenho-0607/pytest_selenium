
from src.web.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class NotePage(BasePage):
    def __init__(self, elements):
        super().__init__(elements)

    username_txt = (By.ID, "login-form-username")
    password_txt = (By.ID, "txtPassword")
    signin_btn = (By.XPATH, "//button[text()='Sign In']")
