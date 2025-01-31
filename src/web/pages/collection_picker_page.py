from selenium.webdriver.common.by import By

from src.data.enum import Collections
from src.utils.common_util import cook_element
from src.web.pages.base_page import BasePage


class CollectionPicker(BasePage):
    def __init__(self, elements):
        super().__init__(elements)

    # smart, shared, my collections
    # _collection_toggle = (By.XPATH, '//span[text()[normalize-space()="{}"]]')
    _new_icon = (
        By.XPATH, '//span[text()[normalize-space()="{}}"]]/parent::div//i[@class="icon-plus-large"]'
    )

    # new collection form
    _collection_name_input = (By.CSS_SELECTOR, '(//input[@placeholder="Untitled Collection"])[last()]')
    _create_collection_btn = (By.XPATH, '//button[@type="submit"]/span[text()="Create Collection"]')
    _make_shared_col_checkbox = (
        By.XPATH, '//span[normalize-space(text())="Make Shared Collection"]'
                  '//following::div[contains(@class, "checkbox")]'
    )

    def create_shared_collection_at_shared_collections(self, collection_name):
        ele = cook_element(self._new_icon, Collections.Type.SHARED_COLLECTIONS)
        self._elements.click(ele)
        self._elements.send_keys(self._collection_name_input, collection_name)
        self._elements.click(self._create_collection_btn)

    def create_shared_collection_at_my_collections(self, collection_name):
        ele = cook_element(self._new_icon, Collections.Type.MY_COLLECTIONS)
        self._elements.click(ele)
        self._elements.send_keys(self._collection_name_input, collection_name)
        self._elements.click(self._make_shared_col_checkbox)
        self._elements.click(self._create_collection_btn)
