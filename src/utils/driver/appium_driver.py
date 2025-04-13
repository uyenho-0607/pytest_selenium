import subprocess

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.options.mac import Mac2Options
from appium.webdriver.appium_service import AppiumService
from selenium.common import WebDriverException

from src.data.project_info import DriverList
from src.utils.logging_util import logger


def start_appium_server(*, host="localhost", port=4723, wda_port=8100):
    # https://appium.io/docs/en/writing-running-appium/server-args/
    kill_command = f"lsof -ti :{port} | xargs kill -9"

    subprocess.run(kill_command, shell=True, check=True)
    subprocess.run(f"lsof -ti :{wda_port} | xargs kill -9", shell=True, check=True)

    appium_service = AppiumService()
    args = [
        "-pa", "/wd/hub",
        "--address", host,
        "--port", str(port),
        "--driver-xcuitest-webdriveragent-port", str(wda_port),
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
    options.platform_name = "iOS"
    options.platform_version = "17.2"  # simulator
    options.device_name = "iPhone 15"  # simulator
    # options.udid = "00008101-00044C5A21F8001E"  # real device
    options.bundle_id = "com.floware.flo.staging"
    # options.automation_name = "XCUITest"
    options.app = "/Users/uyenhn/Downloads/apps/FloiOS_0.9.52_202403141200.app"
    options.new_command_timeout = 30000
    # options.use_new_wda = False
    # options.use_prebuilt_wda = True
    options.no_reset = True
    options.full_reset = False

    DriverList.appium_service = start_appium_server()

    try:
        driver = webdriver.Remote(f"http://localhost:{port}/wd/hub", options=options)
        DriverList.appium_driver.append(driver)
        return driver

    except WebDriverException as ex:
        error = f"Failed to init resources driver with error: {ex}"
        logger.error(error)
        raise WebDriverException(error)


def init_mac_driver(port=4724):

    # subprocess.run(f"lsof -ti :{port} | xargs kill -9", shell=True, check=True)

    options = Mac2Options()
    options.platform_name = "mac"
    options.automation_name = "mac2"
    options.bundle_id = "com.floware.flomac.internal"
    options.new_command_timeout = 30000
    # DriverList.appium_service = start_appium_server(port=port)
    port = 4723

    try:

        # driver = webdriver.Remote(f"http://localhost:{port}/wd/hub", options=options)
        # driver = webdriver.Remote(f"http://172.16.49.12:{port}/wd/hub", options=options)
        driver = webdriver.Remote(f"http://172.16.49.12:{port}", options=options)
        DriverList.appium_driver.append(driver)

        return driver

    except WebDriverException as ex:
        error = f"Failed to init resources driver with error: {ex}"
        logger.error(error)
        raise WebDriverException(error)
