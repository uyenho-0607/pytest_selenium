import time

from src.utils.common_util import random_sentence
from src.utils.logging_util import logger


def test(pages, close_call_view):
    channel_title = random_sentence()
    channel_title = "Random sentence - ZLaxnGKU7f"

    # logger.info("- Add channel")
    # pages.channels_pages.create_channel(channel_title)
    #
    # logger.info("- Add participant")
    # pages.channels_pages.call_view.add_participant("auto763e90_web_test")

    logger.info("- send chat message")
    pages.channels_pages.open_channel(channel_title)
    for i in range(20):
        pages.channels_pages.chat_panel.send_message(f"{random_sentence()} #{i+1}")
        time.sleep(0.5)
