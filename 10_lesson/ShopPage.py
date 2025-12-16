from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ShopPage():
    def __init__(self, driver) -> None:
        """
        Инициализация страницы магазина.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
    
    @allure.step("Нажать на кнопки для выбора товаров")      
    def add_to_cart(self) -> None:
        """
        Добавляет несколько товаров в корзину,
        нажимая кнопки 'Add to cart' у товаров на странице.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        
    @allure.step("Нажать на кнопку корзины")      
    def get_to_cart(self) -> None:
        """
        Переходит на страницу корзины, нажимая на иконку корзины в шапке сайта.
        """
        cart_link = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link")))
        cart_link.click()