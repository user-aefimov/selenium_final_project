# pages/base_page.py
# Базовый класс для Page Object, содержащий общие методы
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=10):  # Конструктор класса, принимающий браузер и URL
        self.browser = browser  # Сохраняем экземпляр браузера для дальнейшего использования
        self.url = url  # Сохраняем URL страницы
        self.browser.implicitly_wait(timeout)

        
    def open(self):  # Метод для открытия страницы по сохраненному URL
        self.browser.get(self.url)  # Используем метод get() браузера для загрузки страницы


    def is_element_present(self, how, what):
        self.what = what
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
   
