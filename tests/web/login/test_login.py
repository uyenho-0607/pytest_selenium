from src.data.project_info import ProjectInfo
from src.utils.logging_util import logger


def test(pages):
    data = ProjectInfo

    logger.info("Step 1: perform login")
    pages.login_page.login(data.user, data.password)

    logger.info("Verify login succeeded")
    pages.home_page.verify_login_succeeded()

