from src.utils.common_util import random_title
from src.utils.logging_util import logger


def test(pages, close_call_view):
    channel_title = random_title()
    participant_1 = "auto763e90_web_test1"
    participant_2 = "auto763e90_web_test2"

    logger.info(f"Step 1: Create channel with title: {channel_title!r}")
    pages.channels_pages.create_channel(channel_title)

    logger.info(f"Step 2: Add participant 1: {participant_1}")
    pages.channels_pages.call_view.add_participant(participant_1)

    logger.info("Verify participant 1 is displayed in call view")
    pages.channels_pages.call_view.verify_participant_is_displayed(participant_1)

    logger.info(f"Step 3: Add participant 2: {participant_1}")
    pages.channels_pages.call_view.add_participant(participant_2)

    logger.info("Verify participant 2 is displayed in call view")
    pages.channels_pages.call_view.verify_participant_is_displayed(participant_2)
