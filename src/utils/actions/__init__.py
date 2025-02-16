from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.data.logs import MsgLog
from src.utils import allure_util
from src.utils.assert_util import soft_assert
from src.utils.logging_util import logger


class BaseActions:

    def __init__(self, driver):
        self._driver = driver
        # self._driver.implicitly_wait(time_to_wait=3)
        self._wait = WebDriverWait(self._driver, 10)
        self._action_chain = ActionChains(self._driver)

    def __find_element__(self, locator: tuple, timeout=None) -> WebElement:
        wait = WebDriverWait(self._driver, timeout=timeout) if timeout else self._wait
        try:
            return wait.until(EC.visibility_of_element_located(locator))

        except Exception as e:

            logger.error(f"Element with locator {locator} not found !")
            raise Exception(f"Element with locator {locator} not found !") from e

    def __find_elements__(self, locator: tuple, timeout=None) -> list[WebElement]:
        wait = WebDriverWait(self._driver, timeout=timeout) if timeout else self._wait
        try:
            return wait.until(EC.visibility_of_all_elements_located(locator))

        except Exception as e:

            logger.error(f"Elements with locator {locator} not found!")
            MsgLog.is_broken = True
            allure_util.capture_and_attach_screenshot(self._driver, name="broken")

            raise Exception(f"Elements with locator {locator} not found!") from e

    def safe_find_element(self, locator: tuple, timeout=None, retries=1) -> WebElement:

        for i in range(retries):
            try:
                ele = self.__find_element__(locator, timeout=timeout)
                if ele:
                    return ele

            except Exception:
                logger.debug(f"Attempt {i + 1}/{retries} failed for locator {locator}")

        MsgLog.is_broken = True
        allure_util.capture_and_attach_screenshot(self._driver, name="broken")
        raise Exception(f"Element not found after {retries} attempt(s)")

    def safe_find_elements(self, locator: tuple, timeout=None, retries=1) -> list[WebElement]:

        for i in range(retries):
            try:
                ele = self.__find_elements__(locator, timeout=timeout)
                if ele:
                    return ele

            except Exception:
                logger.debug(f"Attempt {i + 1}/{retries} failed for locator {locator}")

        raise Exception(f"Elements not found after {retries} attempt(s)")

    def _is_displayed(self, locator: tuple, timeout=None):

        try:
            wait = self._wait
            if timeout:
                wait = WebDriverWait(self._driver, timeout=timeout)

            element = wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()

        except TimeoutException:

            return False

    def click(self, locator: tuple, timeout=None, retries=1):
        ele = self.safe_find_element(locator, timeout, retries)
        ele.click()

    def click_by_offset(self, locator: tuple, timeout=None, x_offset=0, y_offset=0):
        ele = self.safe_find_element(locator, timeout=timeout)
        self._action_chain.move_to_element_with_offset(ele, x_offset, y_offset).click().perform()

    def send_keys(self, locator, keys, timeout=None, retries=1):
        ele = self.safe_find_element(locator, timeout, retries)
        ele.send_keys(keys)

    def send_keys_and_press_enter(self, locator, keys, timeout=None, retries=1):
        ele = self.safe_find_element(locator, timeout, retries)
        ele.send_keys(keys, Keys.ENTER)

    def enter(self):
        self._action_chain.send_keys(Keys.ENTER)

    def get_attribute(self, locator: tuple, attribute, timeout=None):
        ele = self.safe_find_element(locator, timeout)
        return ele.get_attribute(attribute)

    # ------- Mouse Movement ----- #
    def right_click(self, locator: tuple, timeout=None, retries=1):
        ele = self.safe_find_element(locator, timeout, retries)
        self._action_chain.context_click(ele).perform()

    def double_click(self, locator: tuple, timeout=None, retries=1):
        ele = self.safe_find_element(locator, timeout, retries)
        self._action_chain.double_click(ele).perform()

    def hover(self, locator: tuple, timeout=None, retries=1):
        ele = self.safe_find_element(locator, timeout, retries)
        self._action_chain.move_to_element(ele).perform()

    def drag_and_drop(self, locator_1: tuple, locator_2: tuple, timeout=None):
        ele_1 = self.safe_find_element(locator_1, timeout=timeout)
        ele_2 = self.safe_find_element(locator_2, timeout=timeout)
        self._action_chain.drag_and_drop(ele_1, ele_2).perform()

    def force_click(self, locator, timeout=None):
        ele = self.safe_find_element(locator, timeout)
        self._driver.execute_script("arguments[0].click();", ele)

    # ----- Verify ------ #
    def verify_is_displayed(self, locator: tuple, timeout=None):
        res = self._is_displayed(locator, timeout=timeout)
        soft_assert(res, True, f"Element {locator} is not displayed")

    def verify_has_text(self, locator: tuple, expected, timeout=None):
        ele = self.safe_find_element(locator, timeout)
        actual = ele.get_attribute("textContent").strip()
        soft_assert(actual == expected, True, f"{actual!r} is different from {expected!r}")


class Appium(BaseActions):
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
