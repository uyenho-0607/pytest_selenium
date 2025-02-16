from selenium.webdriver.common.by import By

from src.data.enums import Emojis
from src.web.pages.base_page import BasePage

class ChatPanel(BasePage):
    def __init__(self, actions):
        super().__init__(actions)

    __chat_title = (By.CSS_SELECTOR, "//span[@class='header-title' and text()='Chat']")
    __type_message_placeholder = (By.CSS_SELECTOR, ".fr-element.fr-view.fr-element-scroll-visible")
    __emoji_chat_box = (By.CSS_SELECTOR, "*[type='button'][title='Emoticons']")
    __emoji_list = (By.CSS_SELECTOR, ".emoji-list span")

    def send_message(self, message):
        self.actions.send_keys_and_press_enter(self.__type_message_placeholder, message, retries=3)

    def open_emoji_chat_box(self):
        if self.actions.get_attribute(self.__emoji_chat_box, "aria-expanded") == "false":
            self.actions.click(self.__emoji_chat_box)

    def send_emojis(self, emojis: Emojis | list[Emojis]):
        self.open_emoji_chat_box()

        emoji_list = emojis if isinstance(emojis, list) else [emojis]
        send_time = len(emoji_list)

        for option in self.actions.safe_find_elements(self.__emoji_list, retries=3):
            if option.get_attribute("title") in emoji_list:
                option.click()
                send_time -= 1

            if not send_time:
                break

        self.send_message("")

    def verify_panel_is_opened(self):
        self.actions.verify_is_displayed(self.__chat_title)
