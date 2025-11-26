from selenium import webdriver
from AuthPage import AuthPage
from ShopPage import ShopPage
from CartPage import CartPage
from OrderPage import OrderPage

def test_shop():
    browser = webdriver.Firefox()
    auth_page = AuthPage(browser)
    auth_page.open()
    auth_page.get_login("standard_user")
    auth_page.get_password("secret_sauce")
    auth_page.submit_button()
    
    shop_page = ShopPage(browser)
    shop_page.add_to_cart()
    shop_page.get_to_cart()
    
    cart_page = CartPage(browser)
    cart_page.checkout_button()
    
    order_page = OrderPage(browser)
    order_page.fill_form()
    order_page.submit_form()
    order_page.get_total_price()
    
    browser.quit()

