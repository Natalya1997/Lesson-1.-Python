from selenium import webdriver
from AuthPage import AuthPage
from ShopPage import ShopPage
from CartPage import CartPage
from OrderPage import OrderPage
import allure


@allure.title("Тестирование работы магазина")
@allure.severity("Blocker")
@allure.description("Тест проверяет корректность авторизации,выбора товаров, добавление их в корзину и оформление покупки")
@allure.feature("Shop")
def test_shop():
    """
    Тест проверяет, что сайт позволяет авторизоваться,
    добавить выбранные товары в корзину, перейти в нее
    и заполнить форму для оформления покупки.
    """
    with allure.step("Открыть браузер"):
        browser = webdriver.Firefox()
    with allure.step("Открыть страницу авторизации"):
        auth_page = AuthPage(browser)
        auth_page.open()
    with allure.step("Ввести логин"):
        auth_page.get_login("standard_user")
    with allure.step("Ввести пароль"):
        auth_page.get_password("secret_sauce")
    with allure.step("Нажать на кнопку 'submit'"):
        auth_page.submit_button()
    
    with allure.step("Добавить товары в корзину"):
        shop_page = ShopPage(browser)
        shop_page.add_to_cart()
    with allure.step("Перейти в корзину"):
        shop_page.get_to_cart()
        
    with allure.step("Нажать на кнопку 'checkout'"):
        cart_page = CartPage(browser)
        cart_page.checkout_button()
        
    with allure.step("Заполнить форму оформления заказа"):
        order_page = OrderPage(browser)
        order_page.fill_form()
    with allure.step("Нажать на кнопку 'submit'"):
        order_page.submit_form()
    with allure.step("Получить общую сумму"):
        price = order_page.get_total_price()
        assert price == "Total: $58.29"
    
    with allure.step("Закрыть браузер"):
        browser.quit()