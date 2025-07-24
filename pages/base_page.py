# pages/base_page.py
# Базовый класс для Page Object, содержащий общие методы
import math
import re
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
import time

class BasePage():
    def __init__(self, browser, url, timeout=10):  # Конструктор класса, принимающий браузер и URL
        self.browser = browser  # Сохраняем экземпляр браузера для дальнейшего использования
        self.url = url  # Сохраняем URL страницы
        self.browser.implicitly_wait(timeout)

        
    def open(self):  # Метод для открытия страницы по сохраненному URL
        self.browser.get(self.url)  # Используем метод get() браузера для загрузки страницы


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

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_element_present(self, how, what):
        self.what = what
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
   
