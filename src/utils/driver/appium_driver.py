import subprocess

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.options.mac import Mac2Options
from appium.webdriver.appium_service import AppiumService
from selenium.common import WebDriverException

from src.data.project_info import DriverList
from src.utils.logging_util import logger


def start_appium_server(*, host="localhost", port=4723):
    # https://appium.io/docs/en/writing-running-appium/server-args/
    kill_command = f"lsof -ti :{port} | xargs kill -9"
    subprocess.run(kill_command, shell=True, check=True)
    appium_service = AppiumService()
    args = [
        "-pa", "/wd/hub",
        "--address", host,
        "--port", str(port),
    ]

    logger.debug("- Starting appium server... ")
    appium_service.start(args=args, timeout_ms=10000)
    logger.debug("- Started appium server !")

    if not appium_service.is_running:
        error = f"Failed to start Appium server '{host}:{port}'"
        logger.error()
        raise Exception(error)
    return appium_service


def init_appium_driver(port=4723):
    # https://appium.io/docs/en/2.0/guides/caps/

    options = XCUITestOptions()
    options.platform_name = "iOs"
    options.platform_version = "17.2"
    options.device_name = "iPhone 15"
    options.automation_name = "XCUITest"
    options.app = "/Users/uyenhn/Downloads/apps/FloiOS_0.9.52_202403141200.app"
    options.new_command_timeout = 30000
    DriverList.appium_service = start_appium_server()

    try:
        driver = webdriver.Remote(f"http://localhost:{port}/wd/hub", options=options)
        DriverList.appium_driver.append(driver)
        return driver

    except WebDriverException as ex:
        error = f"Failed to init resources driver with error: {ex}"
        logger.error(error)
        raise WebDriverException(error)


def init_mac_driver(port=4723):

    system_port = 4724
    kill_command = f"lsof -ti :{system_port} | xargs kill -9"
    subprocess.run(kill_command, shell=True, check=True)

    options = Mac2Options()
    options.platform_name = "mac"
    options.automation_name = "mac2"
    options.bundle_id = "com.floware.flomac.internal"
    options.system_port = system_port
    options.new_command_timeout = 30000
    DriverList.appium_service = start_appium_server()

    try:

        driver = webdriver.Remote(f"http://localhost:{port}/wd/hub", options=options)
        DriverList.appium_driver.append(driver)

        return driver

    except WebDriverException as ex:
        error = f"Failed to init resources driver with error: {ex}"
        logger.error(error)
        raise WebDriverException(error)
