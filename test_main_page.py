# test_main_page.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License

# Импортируем необходимые модули для работы с Selenium
import pytest
from selenium.webdriver.common.by import By  # Способ поиска элементов на странице (например, по ID или CSS)
from selenium.webdriver.support.ui import WebDriverWait  # Инструмент для ожидания загрузки элементов
from selenium.webdriver.support import expected_conditions as EC  # Условия ожидания (например, видимость элемента)
from pages.main_page import MainPage  # Импортируем класс MainPage из пакета pages
from pages.login_page import LoginPage  # Импортируем класс LoginPage из пакета pages
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # Определяем тест, проверяющий переход на страницу логина
    def test_guest_can_go_to_login_page(self, browser):  # 'browser' — фикстура из conftest.py, предоставляющая экземпляр браузера
        # Указываем URL тестируемой страницы
        # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        link = "http://selenium1py.pythonanywhere.com/"
        # Создаем экземпляр класса MainPage, передавая браузер и URL
        # MainPage — это Page Object, который инкапсулирует логику работы с главной страницей
        page = MainPage(browser, link)
        # Открываем страницу, используя метод open() из BasePage
        page.open()
        # Выполняем переход на страницу логина, используя метод go_to_login_page()
        # login_page = page.go_to_login_page()
        # login_page.should_be_login_page()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.basket 
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # 1. Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # 2. Переходит в корзину по кнопке в шапке сайта
    basket_page = page.go_to_basket_page()
    # 3. Ожидаем, что в корзине нет товаров
    # 4. Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket()





# def test_login_page(browser):
#     page = LoginPage(browser, url="http://selenium1py.pythonanywhere.com/accounts/login/")
#     page.open()
#     page.should_be_login_page()