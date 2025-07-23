# test_main_page.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License

# Импортируем необходимые модули для работы с Selenium
from selenium.webdriver.common.by import By  # Способ поиска элементов на странице (например, по ID или CSS)
from selenium.webdriver.support.ui import WebDriverWait  # Инструмент для ожидания загрузки элементов
from selenium.webdriver.support import expected_conditions as EC  # Условия ожидания (например, видимость элемента)
from .pages.main_page import MainPage  # Импортируем класс MainPage из пакета pages


# Определяем тест, проверяющий переход на страницу логина
def test_guest_can_go_to_login_page(browser):  # 'browser' — фикстура из conftest.py, предоставляющая экземпляр браузера
    # Указываем URL тестируемой страницы
    link = "http://selenium1py.pythonanywhere.com/"
    # Создаем экземпляр класса MainPage, передавая браузер и URL
    # MainPage — это Page Object, который инкапсулирует логику работы с главной страницей
    page = MainPage(browser, link)
    # Открываем страницу, используя метод open() из BasePage
    page.open()
    # Выполняем переход на страницу логина, используя метод go_to_login_page()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()