import builtins
from src.utils.elements import Appium


class MobileElements(Appium):
    def __init__(self, driver=None):
        self.driver = driver or builtins.mobile_driver
        super().__init__(driver)

    # Mobile actions
    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        self._driver.swipe(start_x, start_y, end_x, end_y, duration=duration)

    # appium
    def scroll_to_element(self, locator, timeout=None):
        ele = self._find_element(locator, timeout=timeout)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", ele)

    def drag_and_drop(self, locator_1: tuple, locator_2: tuple, timeout=None):
        ele_1 = self._find_element(locator_1, timeout=timeout)
        ele_2 = self._find_element(locator_2, timeout=timeout)
        self._driver.drag_and_drop(ele_1, ele_2)

    def back(self):
        self._driver.back()

    def forward(self):
        self._driver.forward()

    def long_press(self, locator):
        ...

    def tap(self, locator):
        ...
