# conftest.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License

import pytest  # Импортируем pytest для настройки тестов
from selenium import webdriver  # Импортируем Selenium для управления браузером
from selenium.webdriver.chrome.service import Service as ChromeService  # Сервис для Chrome
from selenium.webdriver.firefox.service import Service as FirefoxService  # Сервис для Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions  # Настройки для Chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions  # Настройки для Firefox
from webdriver_manager.chrome import ChromeDriverManager  # Менеджер для ChromeDriver
from webdriver_manager.firefox import GeckoDriverManager  # Менеджер для GeckoDriver
import logging


def pytest_configure(config):
    # Базовый уровень логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # logging.INFO - только основные действия
    # logging.DEBUG - детальная информация
    # logging.WARNING - только предупреждения и ошибки
    
    # Для конкретных модулей можно установить разный уровень
    logging.getLogger('login_page').setLevel(logging.DEBUG)

# Функция для добавления пользовательских опций при запуске pytest
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', 
                     help="Choose language: ru, en-gb, es")

# Фикстура для создания и настройки браузера
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")  # Получаем имя браузера из командной строки
    user_language = request.config.getoption('language')  # Получаем язык из командной строки
    browser = None
    options = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")  # Сообщаем о запуске Chrome
        options = ChromeOptions()
        options.add_argument(f"--lang={user_language}")  # Устанавливаем язык интерфейса
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # Устанавливаем предпочтительный язык
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")  # Сообщаем о запуске Firefox
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)  # Устанавливаем предпочтительный язык
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser  # Передаем браузер в тест
    print("\nquit browser..")  # Сообщаем о закрытии браузера
    browser.quit()