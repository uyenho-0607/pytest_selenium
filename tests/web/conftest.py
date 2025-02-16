import pytest

from src.utils.actions.web import WebActions
from src.web.pages.channels_page import ChannelsPage
from src.web.pages.home_page import HomePage
from src.web.pages.login_page import LoginPage
from src.web.pages.collection_picker_page import CollectionPicker


@pytest.fixture(scope="session")
def pages():
    web_actions = WebActions()
    loginPage = LoginPage(web_actions)
    homePage = HomePage(web_actions)
    channelsPage = ChannelsPage(web_actions)
    collectionPicker = CollectionPicker(web_actions)

    class PageContainer:
        login_page = loginPage
        home_page = homePage
        channels_pages = channelsPage
        collection_picker = collectionPicker

    return PageContainer
