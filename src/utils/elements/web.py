import builtins
from src.utils.elements import Elements


class WebElements(Elements):
    def __init__(self, driver=None):
        super().__init__(driver or builtins.web_driver)

