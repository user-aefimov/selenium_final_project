# login_page.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License


# Класс для работы со страницей логина, наследуется от BasePage

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
        
    def register_new_user(self, email, password):
        # Заполняем форму регистрации
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)

        # password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        # password_field.send_keys(password)

        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field1.send_keys(password)
        
        password_field2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        password_field2.send_keys(password)

        # Нажимаем кнопку регистрации
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_registered(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_SUCCESS
        ), "Registration failed"