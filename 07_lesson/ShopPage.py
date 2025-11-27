from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage():
    def __init__(self, driver):
        self._driver = driver
        
    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        
        
    def get_to_cart(self):
        cart_link = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable(By.CSS_SELECTOR, "a.shopping_cart_link"))
        cart_link.click()