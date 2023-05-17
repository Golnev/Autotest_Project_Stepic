from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """"Проверка на корректный url адрес"""
        assert self.browser.current_url == LoginPageLocators.LOGIN_PAGE_URL, 'url address is not correct'

    def should_be_login_form(self):
        """Проверка, что есть форма логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is not presented'

    def should_be_register_form(self):
        """Проверка, что есть форма регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is not presented'

    def register_new_user(self, email: str, password: str):
        """Регистрация пользователя"""
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_form.send_keys(email)

        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_form.send_keys(password)

        password_confirm_form = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        password_confirm_form.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
