# locators.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License

from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_SUCCESS = (By.CSS_SELECTOR, ".alert-success")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:first-child .alertinner")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:first-child .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info .alertinner p:first-child")
    
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")  # Первый алерт: "Coders at Work был добавлен в вашу корзину"
    # BASKET_PROMO_ALERT = (By.XPATH, "//div[contains(text(), 'Deferred benefit offer')]")  # Второй алерт
    # BASKET_TOTAL = (By.XPATH, "//p[contains(text(), 'Стоимость корзины теперь составляет')]/strong")  # Третий алерт
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")  
    # BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info p strong")   
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success .alertinner strong")
    # BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info .alertinner strong")
    # SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]//strong")
    # BASKET_TOTAL = (By.XPATH, "//div[contains(@class, 'alert-info')]//strong")
    # # Универсальный локатор для сообщения об успехе
    # SUCCESS_MESSAGE = (By.XPATH, 
    #     "//div[contains(@class, 'alertinner') and contains(., 'has been added') or "
    #     "contains(., 'был добавлен')]")
    # # Универсальный локатор для стоимости корзины
    # BASKET_TOTAL = (By.XPATH, 
    #     "//div[contains(@class, 'alertinner')]//strong[contains(., '£')] | "
    #     "//div[@id='messages']//div[contains(., 'basket total')]//strong")
    
    