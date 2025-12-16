from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage():
    def __init__(self, driver):
        self._driver = driver
      
    def checkout_button(self):
        checkout_button = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
        checkout_button.click()
        