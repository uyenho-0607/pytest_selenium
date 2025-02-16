from selenium.webdriver.common.by import By

from src.utils.common_util import cook_element
from src.web.components.chat_panel import ChatPanel
from src.web.components.workspace.channel_view import ChannelView
from src.web.components.context_menu.channels import ChannelsContextMenu
from src.web.components.settings.channels import ChannelsSettings
from src.web.components.panel_navigation.channels import ChannelsPanelNavigation
from src.web.components.panel_local_filter.channels import ChannelsLocalFilter
from src.web.pages.base_page import BasePage


class ChannelsPage(BasePage):
    def __init__(self, actions):
        super().__init__(actions)
        self.call_view = ChannelView(actions)
        self.chat_panel = ChatPanel(actions)
        self.context_menu = ChannelsContextMenu(actions)
        self.settings = ChannelsSettings(actions)
        self.navigation = ChannelsPanelNavigation(actions)
        self.local_filter = ChannelsLocalFilter(actions)

    __add_call_icon = (By.CSS_SELECTOR, "i.icon-add-call")
    __channel_item_list = (By.CSS_SELECTOR, "*[class^='channel-name'][title='{}']")
    __search_box = (By.ID, "channel-search-input")
    __call_icon = (
        By.XPATH, "//span[@title='{}']/ancestor::div[contains(@class, 'infobox-item-wrapper')]"
                  "//i[contains(@class, 'icon-call-line')]"
    )
    __chat_icon = (
        By.XPATH, "//span[@title='{}']/ancestor::div[contains(@class, 'infobox-item-wrapper')]"
                  "//i[contains(@class, 'icon-comment-lines')]"
    )

    def open_channel(self, title):
        ele = cook_element(self.__channel_item_list, title)
        self.actions.click(ele)

    def create_channel(self, title=""):
        self.actions.click(self.__add_call_icon)
        if title:
            self.call_view.edit_channel_title(title)

    def create_channel_with_participants(self, participants: list[str], title=""):
        self.actions.click(self.__add_call_icon)
        if title:
            self.call_view.edit_channel_title(title)

        self.call_view.add_participants(participants)

    def search(self, search_text):
        self.actions.send_keys_and_press_enter(self.__search_box, search_text)

    def open_chat_panel(self, title):
        self.actions.click(cook_element(self.__chat_icon, title))

    def verify_channel_is_displayed(self, title):
        self.actions.verify_is_displayed(cook_element(self.__channel_item_list, title))
