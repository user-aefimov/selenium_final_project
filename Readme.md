# Автоматизированное тестирование веб-приложений

Проект предоставляет фреймворк для кросс-браузерного и мультиязычного тестирования веб-приложений с использованием Selenium и pytest.

## 📦 Технологический стек
- **Python** (версия 3.7+)
- **Selenium WebDriver**
- **Pytest** (тестовый фреймворк)
- **WebDriver Manager** (автоматическое управление драйверами)
- **Chrome** и **Firefox** (поддерживаемые браузеры)

Установка
Клонируйте репозиторий:
git clone https://github.com/user-aefimov/selenium_final_project.git
cd selenium_final_project

## ⚙️ Установка зависимостей
```bash
pip install -r requirements.txt
Содержимое requirements.txt:

txt
selenium>=4.0
pytest>=7.0
webdriver-manager>=3.0
🚀 Запуск тестов
Базовый запуск (Chrome, английский язык)
bash
pytest
С параметрами:
bash
pytest -v --tb=line --language=en test_main_page.py
pytest --browser_name=firefox --language=fr test_main_page.py

Доступные опции:
Параметр	Значения по умолчанию	Описание
--browser_name	chrome	Браузер: chrome или firefox
--language	en-gb	Язык интерфейса: ru, es, fr, pt, it
📂 Структура проекта
text
project-root/
├── conftest.py            # Конфигурация тестового окружения
├── test_items.py          # Тесты элементов интерфейса
├── test_main.py           # Основные функциональные тесты
├── README.md              # Документация (этот файл)
└── requirements.txt       # Зависимости проекта


#### 5. Дополнение `pages/base_page.py`
Для поддержки методов поиска элементов в Page Object:
```python
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        
    def find_element(self, by, locator):
        """Обертка для поиска элемента"""
        return self.browser.find_element(by, locator)

6. Обновление pages/main_page.py
python
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.find_element(By.CSS_SELECTOR, "#login_link")  # Используем метод из BasePage
        login_link.click()

🔧 Основные компоненты
conftest.py
Центральная конфигурация тестов с фикстурами для:
Инициализации браузера (Chrome/Firefox)
Автоматической настройки языков
Управления жизненным циклом драйвера
Параметризации через командную строку


test_main.py
Функциональные тесты:
Переходы между страницами
Работа с формами
Проверки контента

Кросс-браузерная совместимость
🌍 Особенности реализации
Автоматическое управление драйверами
ChromeDriver и GeckoDriver устанавливаются автоматически
Всегда используются актуальные версии драйверов
Поддержка мультиязычности
Тесты запускаются на 6+ языках
Проверка атрибута lang в HTML
Верификация локализованных текстов
Кросс-браузерное тестирование
Единая кодовая база для Chrome и Firefox
Параллельный запуск в разных браузерах
Профессиональные практики тестирования
Явные ожидания элементов (WebDriverWait)
Изолированные тесты (фикстуры с scope=function)
Детализированные сообщения об ошибках

📄 Лицензия
Проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.