import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину:

def test_has_add_to_card_button(browser):
    browser.get(link)

    # time.sleep(30)

    cart_button = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(cart_button) > 0, 'cart button not found' 


# запуск теста с передачей параметров (например, язык - испанский) в командной строке: 
# pytest -s -v --language=es test_items.py




