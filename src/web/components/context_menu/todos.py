from src.web.components.context_menu.base import BaseContextMenu


class TodosContextMenu(BaseContextMenu):
    def __init__(self, actions):
        super().__init__(actions)
