from selenium.webdriver.common.by import By

from src.data.project_info import ProjectInfo
from src.utils.assert_util import soft_assert
from src.utils.common_util import cook_element
from src.web.components.workspace.base import BaseWorkspace


class ChannelView(BaseWorkspace):
    def __init__(self, actions):
        super().__init__(actions)

    __participant_search_box = (By.ID, "participant-search-box")
    __call_title = (By.CSS_SELECTOR, ".call-title")
    __edit_title_icon = (By.CSS_SELECTOR, "i[class^='icon-edit']")
    __edit_channel_title = (By.CSS_SELECTOR, "input[class^='edit-channel-title']")
    __participant_info = (
        By.XPATH, "//*[contains(@class, 'participant-info') and contains(@title, '{}')]"
    )

    def edit_channel_title(self, title):
        self.actions.hover(self.__call_title)
        self.actions.click(self.__edit_title_icon)
        self.actions.send_keys_and_press_enter(self.__edit_channel_title, title)

    def add_participant(self, username: str):
        """
        Adds a single participant.
        :param username: username (not containing @domain)
        """

        email = f"{username}@{ProjectInfo.domain}"
        self.actions.send_keys_and_press_enter(self.__participant_search_box, email)

    def add_participants(self, participants: list[str]):
        """
        Adds multiple participants in one step.
        :param participants: List of usernames (not containing @domain)
        """

        for username in participants:
            self.add_participant(username)
            self.verify_participant_is_displayed(username)

    def verify_participant_is_displayed(self, username: str):
        self.actions.verify_is_displayed(cook_element(self.__participant_info, username.capitalize()))

    def verify_channel_title_is_correct(self, title):
        self.actions.verify_has_text(self.__call_title, title)

