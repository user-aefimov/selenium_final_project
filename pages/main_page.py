# pages/main_page.py
# Класс для работы с главной страницей, наследуется от BasePage

from .base_page import BasePage  # Импортируем базовый класс из того же пакета
from selenium.webdriver.common.by import By  # Импортируем способ поиска элементов
from selenium.common.exceptions import NoSuchElementException

class MainPage(BasePage):  # Наследуемся от BasePage для использования его методов
    def should_be_login_link(self):
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), f"ERROR {self.what} is not presented"
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), f"ERROR {self.what} is not presented"


    def go_to_login_page(self):  # Метод для перехода на страницу логина
        # Находим элемент с селектором #login_link (обычно ссылка для входа)
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        # Кликаем по ссылке для перехода на страницу логина
        login_link.click()

