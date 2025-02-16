from src.utils.actions.web import WebActions


class BasePage:
    def __init__(self, actions):
        self.actions: WebActions = actions
