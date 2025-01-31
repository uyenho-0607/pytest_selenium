from src.utils.elements.web import WebElements


class BasePage:
    def __init__(self, elements):
        self._elements: WebElements = elements
