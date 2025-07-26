import pytest
import time
from .pages.product_page import ProductPage

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
    page.should_contain_success_phrase()
    page.should_be_basket_total(product_price)