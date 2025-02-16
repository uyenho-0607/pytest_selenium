from src.utils.logging_util import logger
from src.utils.common_util import random_title


def test(pages, close_call_view):
    channel_title = random_title()

    logger.info(f"Step: Create channel with title: {channel_title!r}")
    pages.channels_pages.create_channel(channel_title)

    logger.info("Verify channel is displayed in item list")
    pages.channels_pages.verify_channel_is_displayed(channel_title)

    logger.info(f"Verify channel title in call view is {channel_title!r}")
    pages.channels_pages.call_view.verify_channel_title_is_correct(channel_title)
