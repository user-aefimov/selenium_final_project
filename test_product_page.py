# test_product_page.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License

import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage

# @pytest.mark.parametrize('product_link', [
#     "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# ])
# def test_guest_can_add_product_to_basket(browser, product_link):
#     page = ProductPage(browser, product_link)
#     page.open()



# @pytest.mark.parametrize('offer_id', [f"offer{i}" for i in range(0, 10)])
# def test_guest_can_add_product_to_basket(browser, offer_id):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer_id}"
#     print(link)
#     page = ProductPage(browser, link)
#     page.open()


offer_ids = [
    pytest.param(f"offer{i}", marks=pytest.mark.xfail) if i == 7 else f"offer{i}"
    for i in range(0, 10)
]

@pytest.mark.need_review
@pytest.mark.parametrize('offer_id', offer_ids)
def test_guest_can_add_product_to_basket(browser, offer_id):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer_id}"
    print(link)
    page = ProductPage(browser, link)
    page.open()


    # Запоминаем данные продукта Проверяем название и цену перед добавлением
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    print(f"Testing product: {product_name} ({product_price})")
    
    # Добавляем в корзину и решаем задачу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    
    # code = page.solve_quiz_and_get_code()
    # if code:
    #     print(f"Received promo code: {code}")
    # else:
    #     print("No promo code received (expected for some offers)")
    
    # Добавляем задержку для появления сообщений
    time.sleep(1)
    
    # Проверяем сообщения
    page.should_be_success_message(product_name)
    page.should_be_basket_total(product_price)


@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходим на страницу логина
    page.go_to_login_page()

@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # 1. Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # 2. Переходит в корзину по кнопке в шапке
    basket_page = page.go_to_basket_page()
    # 3. Ожидаем, что в корзине нет товаров
    # 4. Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_empty_basket()


@pytest.mark.xfail(reason="Сообщение появляется после добавления товара")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Сообщение не исчезает после появления")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappear_success_message()





@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # 1. Открыть страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        # 2. Зарегистрировать нового пользователя
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time())
        login_page.register_new_user(email, password)
        # 3. Проверить, что пользователь залогинен
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

#     offer_ids = [
#     pytest.param(f"offer{i}", marks=pytest.mark.xfail) if i == 7 else f"offer{i}"
#     for i in range(0, 10)
# ]
#     @pytest.mark.parametrize('offer_id', offer_ids)
#     def test_user_can_add_product_to_basket(self, browser, offer_id):
#         link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={offer_id}"
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        # общая часть теста
        page = ProductPage(browser, link)
        page.open()
        # Запоминаем данные продукта Проверяем название и цену перед добавлением
        product_name = page.get_product_name()
        product_price = page.get_product_price()
        print(f"Testing product: {product_name} ({product_price})")
        # Добавляем в корзину и решаем задачу
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        # Добавляем задержку для появления сообщений
        time.sleep(1)
        # Проверяем сообщения
        page.should_be_success_message(product_name)
        page.should_be_basket_total(product_price)


