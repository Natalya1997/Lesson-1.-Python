from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage():
    def __init__(self, driver):
        self._driver = driver
    
    def fill_form(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Natalya")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Simonova")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("220037")
                
    def submit_form(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
   
    def get_total_price(self):
         total_price = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
         assert total_price == "Total: $58.29"
   
   
    
    