
from src.web.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EventPage(BasePage):
    def __init__(self, elements):
        super().__init__(elements)
