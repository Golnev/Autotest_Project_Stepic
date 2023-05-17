from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def item_added_to_basket(self):
        self.add_item_to_basket()
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text.split(' ')[2].split('\n')[0]
        assert product_price == basket_price, \
            f'wrong value of item in basket (received "{basket_price}", expected "{product_price}")'

    def add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()


