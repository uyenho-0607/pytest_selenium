import builtins

import allure
import pytest

from src.data.project_info import ProjectInfo, DriverList
from src.utils import load_config_data
from src.utils.allure_util import log_step_to_allure, custom_allure_report
from src.utils.driver.appium_driver import init_mac_driver, init_appium_driver
from src.utils.driver.web_driver import init_web_driver
from src.utils.logging_util import logger, setup_logging


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", choices=["web", "mac", "ios"], default="web")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--env", action="store", choices=["dev", "staging"], default="staging")


def pytest_sessionstart(session):
    logger.info("============ pytest_sessionstart ============ ")
    setup_logging()
    load_config_data(session.config.getoption("env"))
    prj_info = ProjectInfo

    platform = session.config.getoption("platform")
    headless = session.config.getoption("headless")
    browser = session.config.getoption("browser")

    match platform:
        case "web":
            logger.info("--- init webdriver --- ")
            driver = init_web_driver(browser, headless)
            setattr(builtins, "web_driver", driver)
            driver.get(prj_info.url)

        case "mac":
            logger.info("--- init mac driver --- ")
            driver = init_mac_driver()
            setattr(builtins, "mac_driver", driver)

        case "ios":
            logger.info("--- init appium driver --- ")
            driver = init_appium_driver()
            setattr(builtins, "ios_driver", driver)

        case _:
            raise ValueError("Invalid platform !!!")


def pytest_sessionfinish(session):
    logger.info("============ pytest_sessionfinish ============ ")
    for driver in DriverList.web_driver:
        driver.close()
        driver.quit()

    for driver in DriverList.appium_driver:
        driver.quit()

    if DriverList.appium_service:
        DriverList.appium_service.stop()

    allure_dir = session.config.option.allure_report_dir
    if allure_dir:

        custom_allure_report(allure_dir)
        env_data = {
            "Platform": session.config.getoption("--platform").capitalize(),
            "Environment": session.config.getoption("--env").capitalize()
        }

        with open(f"{allure_dir}/environment.properties", "w") as f:
            for key, value in env_data.items():
                f.write(f"{key}={value}\n")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    logger.info("============ pytest_runtest_makereport ============ ")
    outcome = yield
    report = outcome.get_result()

    # Check if the report is from the 'call' phase
    if report.when == "call":
        log_step_to_allure()
