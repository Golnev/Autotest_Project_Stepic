from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        len_basket_items = len(self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS))
        assert len_basket_items == 0, f'Basket is not empty, {len_basket_items} items in basket'

    def basket_is_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET), 'Basket is empty'

    def basket_empty_massage(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), 'No notification that basket is empty'
