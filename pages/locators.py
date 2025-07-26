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
    

    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:first-child .alertinner")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:first-child .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info .alertinner p:first-child")
    
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")  # Первый алерт: "Coders at Work был добавлен в вашу корзину"
    # BASKET_PROMO_ALERT = (By.XPATH, "//div[contains(text(), 'Deferred benefit offer')]")  # Второй алерт
    # BASKET_TOTAL = (By.XPATH, "//p[contains(text(), 'Стоимость корзины теперь составляет')]/strong")  # Третий алерт
    
    
    # # Универсальный локатор для сообщения об успехе
    # SUCCESS_MESSAGE = (By.XPATH, 
    #     "//div[contains(@class, 'alertinner') and contains(., 'has been added') or "
    #     "contains(., 'был добавлен')]")
    # # Универсальный локатор для стоимости корзины
    # BASKET_TOTAL = (By.XPATH, 
    #     "//div[contains(@class, 'alertinner')]//strong[contains(., '£')] | "
    #     "//div[@id='messages']//div[contains(., 'basket total')]//strong")
    



    


    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")  
    # BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info p strong")   
    # SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success .alertinner strong")
    # BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info .alertinner strong")
    # SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]//strong")
    # BASKET_TOTAL = (By.XPATH, "//div[contains(@class, 'alert-info')]//strong")
    