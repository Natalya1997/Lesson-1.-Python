from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CartPage():
    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
    
    @allure.step("Нажать кнопку 'checkout'")    
    def checkout_button(self) -> None:
        """
        Переходит на страницу оформления заказа, нажимая на кнопку 'checkout'.
        """
        checkout_button = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
        checkout_button.click()
        