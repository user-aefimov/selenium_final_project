import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

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


@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # Переходим на страницу логина
    page.go_to_login_page()

@pytest.mark.basket    
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

