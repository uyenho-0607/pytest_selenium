import pytest

from src.utils.elements.web import WebElements
from src.web.pages.home_page import HomePage
from src.web.pages.login_page import LoginPage


@pytest.fixture(scope="session")
def pages():
    web_elements = WebElements()
    loginPage = LoginPage(web_elements)
    homePage = HomePage(web_elements)

    class PageContainer:
        login_page = loginPage
        home_page = homePage

    return PageContainer
