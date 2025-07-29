# pages/base_page.py
# Базовый класс для Page Object, содержащий общие методы
import math
# import re
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):  # Конструктор класса, принимающий браузер и URL
        self.browser = browser  # Сохраняем экземпляр браузера для дальнейшего использования
        self.url = url  # Сохраняем URL страницы
        self.browser.implicitly_wait(timeout)
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), f"ERROR {self.what} is not presented"
        
    def open(self):  # Метод для открытия страницы по сохраненному URL
        self.browser.get(self.url)  # Используем метод get() браузера для загрузки страницы


    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
                # Попытка обработки алерта, если он появится (старое поведение)
            try:
                # Добавьте ожидание второго алерта (5 секунд)
                WebDriverWait(self.browser, 5).until(EC.alert_is_present())
                alert = self.browser.switch_to.alert
                code_text = alert.text
                print(f"Your code: {code_text}")
                alert.accept()
                print("Обработан промо-алерт (старое поведение)")
                # return code_text  # Возвращаем текст алерта
            except (TimeoutException, NoAlertPresentException):
                print("Промо-алерт не появился (новое поведение)")
                print("No second alert presented")
                # return None
        except Exception as e:
            print(f"Error solving quiz: {str(e)}")
            raise    


    def is_element_present(self, how, what):
        # Устанавливаем неявное ожидание на 0
        self.what = what
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
   
    def is_not_element_present(self, how, what, timeout=4):
        print(f"Checking absence of element: {what} with timeout {timeout} and how {how}")
        self.browser.implicitly_wait(0)
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        print(f"Checking disappear of element: {what} with timeout {timeout} and how {how}")
        self.browser.implicitly_wait(0)
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True
    
    def go_to_basket_page(self):
        from .basket_page import BasketPage
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()
        # Возвращаем объект страницы корзины
        return BasketPage(self.browser, self.browser.current_url)









    # def solve_quiz_and_get_code(self):
    #     try:
    #         alert = self.browser.switch_to.alert
    #         alert_text = alert.text
    #         print(f"Alert text: {alert_text}")

    #         # Извлекаем число после "x ="
    #         match = re.search(r'x\s*=\s*(\d+)', alert_text)
    #         if match:
    #             x = match.group(1)
    #             print(f"Found x = {x}")
    #         # Вычисляем ответ: log10(|12*sin(x)|)
    #             x_rad = math.radians(float(x))
    #             result = math.log10(abs(12 * math.sin(float(x_rad))))
    #             answer = str(round(result, 3))
    #             print(f"Calculated answer: {answer}")
        
    #             # Ввод ответа и подтверждение
    #             alert.send_keys(answer)
    #             time.sleep(3)
    #             alert.accept()
    #             time.sleep(3)
            
    #             # Обработка второго алерта
    #             try:
    #                 alert = self.browser.switch_to.alert
    #                 code_text = alert.text
    #                 print(f"Your code: {code_text}")
    #                 alert.accept()
    #                 return code_text
    #             except NoAlertPresentException:
    #                 print("No second alert presented") 
    #                 return None
    #         else:
    #             print("Couldn't find x value in alert")
    #             return None
                
    #     except Exception as e:
    #         print(f"Error solving quiz: {str(e)}")
    #         raise

    # def clear_basket(driver):
    #     driver.get("https://example.com/basket")
    #     while True:
    #         try:
    #             remove_btn = WebDriverWait(driver, 2).until(
    #                 EC.element_to_be_clickable((By.CSS_SELECTOR, ".remove-item"))
    #             )
    #             remove_btn.click()
    #             WebDriverWait(driver, 2).until(EC.staleness_of(remove_btn))
    #         except TimeoutException:
    #             break