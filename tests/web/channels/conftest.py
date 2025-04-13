import time

import pytest

from src.data.project_info import ProjectInfo
from src.utils.logging_util import logger


@pytest.fixture(scope="package", autouse=True)
def setup(pages):
    data = ProjectInfo

    logger.info("- Perform login")
    pages.login_page.login(data.user, data.password)
    pages.home_page.verify_login_succeeded()

    logger.info("- Open Channels Page")
    pages.home_page.toggle_channels_page()


@pytest.fixture(scope="package", autouse=True)
def teardown(pages):
    yield
    logger.info("- Close Channels Page")
    time.sleep(3)
    pages.home_page.toggle_channels_page(open_page=False)


@pytest.fixture
def close_call_view(pages):
    yield
    logger.info("- Close Call View")
    time.sleep(3)
    pages.channels_pages.call_view.close()
