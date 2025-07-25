from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # Проверка наличия "login" в URL
        assert "login" in self.browser.current_url, \
            f"Current URL is {self.browser.current_url}, but should contain 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # Проверка формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form not found on the page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # Проверка формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form not found on the page"