
import pytest_check as check

from src.data.logs import MsgLog
from src.data.project_info import DriverList
from src.utils import allure_util
from src.utils.logging_util import logger


def soft_assert(*args):
    a, b, msg = args
    res = check.equal(a, b, msg)

    if not res:
        logger.error(msg)

        for driver in DriverList.web_driver:
            allure_util.capture_screenshot(driver)

        failed_msg = check.check_log.get_failures()[-1]
        failed_msg = failed_msg.rsplit(": ", 1)[1]

        failed_step = [item for item in MsgLog.step_logs if "verify" in item.lower()][-1]
        MsgLog.all_failed_logs.append((failed_step, failed_msg))

