from src.data.project_info import ProjectInfo
from src.utils.logging_util import logger


def test(pages):
    data = ProjectInfo

    logger.info("Step 1: perform login")
    pages.login_page.login(data.user, data.password)

    logger.info("Verify login failed 1-1")
    pages.home_page.verify_login_success()

    # logger.info("Verify login success 1-2")
    # pages.login_page.verify_login_success_2()

    logger.info("Step 2: perform login 2 - failed")
    # pages.login_page.login(data.user, data.password)

    logger.info("Verify login failed 2")
    pages.home_page.verify_login_success()

    # logger.info("Verify login success 2")
    # pages.login_page.verify_login_success()

