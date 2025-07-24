import pytest
import time
from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo_offer', ["newYear"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo={promo_offer}"
    page = ProductPage(browser, link)
    page.open()

    # Запоминаем данные продукта Проверяем название и цену перед добавлением
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    print(f"Testing product: {product_name} ({product_price})")
    
    # Добавляем в корзину и решаем задачу
    page.add_to_basket()
    code = page.solve_quiz_and_get_code()
    print(f"Received promo code: {code}")
    
    # Добавляем задержку для появления сообщений
    time.sleep(2)
    
    # Проверяем сообщения
    page.should_be_success_message(product_name)
    page.should_be_basket_total(product_price)