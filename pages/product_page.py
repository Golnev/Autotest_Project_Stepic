from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def item_added_to_basket(self):
        self.add_item_to_basket()
        product_price = self.get_price_of_product()

        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text
        assert product_price == basket_price, \
            f'wrong price of item in basket (received "{basket_price}", expected "{product_price}")'

        name_of_product_title = self.get_name_of_product_title()
        name_of_product_message = self.get_name_of_product_message()
        assert name_of_product_title == name_of_product_message, \
            f'product name does not match the name in the message' \
            f' (name in title - "{name_of_product_title}", name in message - "{name_of_product_message}")'

    def add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    def get_name_of_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TITLE).text

    def get_price_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_name_of_product_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_as_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
