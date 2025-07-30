# login_page.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License


# Класс для работы со страницей логина, наследуется от BasePage

from .base_page import BasePage
from .locators import LoginPageLocators
import logging

logger = logging.getLogger(__name__)

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        logger.info("Checking login URL")
        # реализуйте проверку на корректный url адрес
        # Проверка наличия "login" в URL
        assert "login" in self.browser.current_url, \
            f"Current URL is {self.browser.current_url}, but should contain 'login'"
        logger.debug("URL check passed")

    def should_be_login_form(self):
        logger.info("Checking login form presence")
        # реализуйте проверку, что есть форма логина
        # Проверка формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form not found on the page"
        logger.debug("Login form check passed")

    def should_be_register_form(self):
        logger.info("Checking registration form presence")
        # реализуйте проверку, что есть форма регистрации на странице
        # Проверка формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form not found on the page"
        logger.debug("Registration form check passed")
        
    def register_new_user(self, email, password):
        logger.info(f"Starting registration for new user: {email}")
        
        try:
            # Заполняем форму регистрации
            # Заполнение email
            logger.debug("Locating email field")
            email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
            logger.debug(f"Entering email: {email}")
            email_field.send_keys(email)
            # Заполнение основного поля пароля
            logger.debug("Locating password field")
            password_field1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
            logger.debug("Entering password")
            password_field1.send_keys(password)
            # Заполнение подтверждения пароля
            logger.debug("Locating password cofirmation field")
            password_field2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
            logger.debug("Confirming password")
            password_field2.send_keys(password)

            # Нажимаем кнопку регистрации
            logger.debug("Locating registration button")
            register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
            logger.info("Submiting registration form")
            register_button.click()

            logger.info(f"Registration submitted for user: {email}")
        except Exception as e:
            logger.error(f"Error during registration: {str(e)}")
            logger.exception("Registration failed with exeption")
            raise
        
    def should_be_registered(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_SUCCESS
        ), "Registration failed"