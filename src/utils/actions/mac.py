import builtins
from src.utils.actions import Appium


class MacActions(Appium):
    def __init__(self, driver=None):
        self.driver = driver or builtins.mac_driver
        super().__init__(driver)
