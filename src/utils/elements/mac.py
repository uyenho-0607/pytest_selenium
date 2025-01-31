import builtins
from src.utils.elements import Appium


class MacElements(Appium):
    def __init__(self, driver=None):
        self.driver = driver or builtins.mac_driver
        super().__init__(driver)
