import builtins
from src.utils.actions import BaseActions


class WebActions(BaseActions):
    def __init__(self, driver=None):
        super().__init__(driver or builtins.web_driver)
