from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions

from src.data.project_info import DriverList, ProjectInfo


def init_web_driver(browser, headless=False):

    match browser.lower():
        case "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            driver_class = webdriver.Chrome

        case "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            driver_class = webdriver.Firefox

        case "safari":
            options = SafariOptions()
            if headless:
                options.add_argument("--headless")
            driver_class = webdriver.Safari

        case _:
            raise ValueError("Invalid browser !!! ")

    # driver = webdriver.Remote(command_executor="http://172.16.52.134:4444", options=options)
    driver = driver_class(options=options)
    driver.maximize_window()
    DriverList.web_driver.append(driver)

    return driver
