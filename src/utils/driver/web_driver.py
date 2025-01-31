from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.data.project_info import DriverList

IMPLICITLY_WAIT = 10


def init_web_driver() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    DriverList.web_driver.append(driver)

    return driver
