# conftest.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_can_go_to_login_page(browser, language):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    # Ожидание загрузки страницы
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "login_link"))
    )

    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

    # Проверка языка интерфейса (дополнительная проверка)
    html_lang = browser.find_element(By.TAG_NAME, "html").get_attribute("lang")
    print(f"\nCurrent interface language: {html_lang}")
    assert html_lang == language, f"Язык интерфейса не совпадает: {html_lang} != {language}"

