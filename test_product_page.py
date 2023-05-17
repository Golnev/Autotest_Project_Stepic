from typing import Union

from selenium import webdriver

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.item_added_to_basket()
