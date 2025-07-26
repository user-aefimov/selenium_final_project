from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    
    def should_be_success_message(self, expected_name):
        print("should_be_success_message сработал")
        # Ожидаем появления сообщения
        message_element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        )

        # Получаем текст сообщения
        message = message_element.text
        
        # Проверяем совпадение названия
        assert expected_name == message, f"Product name '{expected_name}' not in success message '{message}'"
    
    def should_be_basket_total(self, expected_price):
        print("should_be_basket_total сработал")
        # Ожидаем появления сообщения о стоимости корзины
        basket_element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located(ProductPageLocators.BASKET_TOTAL)
        )
        
        # Получаем текст сообщения
        basket_total = basket_element.text
        # Проверяем совпадение цены
        assert expected_price in basket_total, f"Product price '{expected_price}' not in basket total '{basket_total}'"