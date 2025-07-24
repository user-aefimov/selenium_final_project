from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:first-child .alertinner")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info .alertinner p:first-child")
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")  # Эти не нашел, чтобы сверить
    # BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info p strong")   # Эти не нашел, чтобы сверить
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success .alertinner strong")
    # BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info .alertinner strong")
    # SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]//strong")
    # BASKET_TOTAL = (By.XPATH, "//div[contains(@class, 'alert-info')]//strong")
    