from typing import Union
import time
import pytest
from selenium import webdriver

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser: Union[webdriver.Chrome, webdriver.Firefox]):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email=email, password='zaq12wsxcde3')

        page.should_be_authorized_user()

    def test_guest_cant_see_success_message(self, browser: Union[webdriver.Chrome, webdriver.Firefox]):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser: Union[webdriver.Chrome, webdriver.Firefox]):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)
        page.open()
        page.item_added_to_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                                  pytest.param(
                                      '"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo'
                                      '=offer7"',
                                      marks=pytest.mark.xfail
                                  ),
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'
                                  ])
def test_guest_can_add_product_to_basket(browser: Union[webdriver.Chrome, webdriver.Firefox], link):
    page = ProductPage(browser, link)
    page.open()
    page.item_added_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.item_added_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_as_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_empty_massage()
