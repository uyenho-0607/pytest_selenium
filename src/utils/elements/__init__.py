from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.data.logs import MsgLog
from src.utils import allure_util
from src.utils.assert_util import soft_assert
from src.utils.logging_util import logger


class Elements:

    def __init__(self, driver):
        self._driver = driver
        # self._driver.implicitly_wait(time_to_wait=3)
        self._wait = WebDriverWait(self._driver, 10)
        self._action_chain = ActionChains(self._driver)

    def _find_element(self, locator: tuple, timeout=None) -> WebElement:
        try:
            wait = self._wait
            if timeout:
                wait = WebDriverWait(self._driver, timeout=timeout)

            return wait.until(EC.visibility_of_element_located(locator))

        except Exception as e:

            logger.error(f"Element with locator {locator} not found !")
            MsgLog.is_broken = True
            allure_util.capture_screenshot(self._driver, name="broken")

            raise Exception(f"Element with locator {locator} not found !") from e

    def _find_elements(self, locator: tuple, timeout=None) -> list[WebElement]:
        try:
            wait = self._wait
            if timeout:
                wait = WebDriverWait(self._driver, timeout=timeout)

            return wait.until(EC.presence_of_all_elements_located(locator))

        except Exception as e:

            logger.error(f"Elements with locator {locator} not found!")
            MsgLog.is_broken = True
            allure_util.capture_screenshot(self._driver, name="broken")

            raise Exception(f"Elements with locator {locator} not found!") from e

    def _is_displayed(self, locator: tuple, timeout=None):

        try:
            wait = self._wait
            if timeout:
                wait = WebDriverWait(self._driver, timeout=timeout)

            element = wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()

        except TimeoutException:

            return False

    def click(self, locator: tuple, timeout=None):
        ele = self._find_element(locator, timeout=timeout)
        ele.click()

    def right_click(self, locator: tuple, timeout=None):
        ele = self._find_element(locator, timeout=timeout)
        self._action_chain.context_click(ele).perform()

    def double_click(self, locator: tuple, timeout=None):
        ele = self._find_element(locator, timeout=timeout)
        self._action_chain.double_click(ele).perform()

    def hover(self, locator: tuple, timeout=None):
        ele = self._find_element(locator, timeout=timeout)
        self._action_chain.move_to_element(ele).perform()

    def drag_and_drop(self, locator_1: tuple, locator_2: tuple, timeout=None):
        ele_1 = self._find_element(locator_1, timeout=timeout)
        ele_2 = self._find_element(locator_2, timeout=timeout)
        self._action_chain.drag_and_drop(ele_1, ele_2).perform()

    def send_keys(self, locator, keys, timeout=None):
        ele = self._find_element(locator, timeout=timeout)
        ele.send_keys(keys)

    def get_attribute(self, locator: tuple, attribute, timeout=None):
        ele = self._find_element(locator, timeout=timeout)
        return ele.get_attribute(attribute)

    def verify_is_displayed(self, locator: tuple, timeout=None):
        res = self._is_displayed(locator, timeout=timeout)
        soft_assert(res, True, f"Element {locator} is not displayed")


class Appium(Elements):
    def __init__(self, driver):
        super().__init__(driver)

    # app
    def active_app(self, app_id):
        self._driver.activate_app(app_id)

    def terminate_app(self, app_id):
        self._driver.terminate_app(app_id)

    def install_app(self, app_path, ):
        self._driver.install_app(app_path=app_path)

    def put_app_background(self, seconds=5):
        self._driver.background_app(seconds)


