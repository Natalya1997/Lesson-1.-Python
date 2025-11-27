from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage():
    def __init__(self, driver):
        self._driver = driver
    
    def fill_form(self):
        first_name = WebDriverWait(self._driver, 20).until(
        EC.visibility_of_element_located(By.CSS_SELECTOR, "#first-name"))
        first_name.send_keys("Natalya")                                 
        last_name = WebDriverWait(self._driver, 20).until(
        EC.visibility_of_element_located(By.CSS_SELECTOR, "#last-name"))
        last_name.send_keys("Simonova")
        post_code = WebDriverWait(self._driver, 20).until(
        EC.visibility_of_element_located(By.CSS_SELECTOR, "#postal-code"))
        post_code.send_keys("220037")
                
    def submit_form(self):
        submit_form = WebDriverWait(self._driver, 10).until(
        EC.element_to_be_clickable(By.CSS_SELECTOR, "#continue"))
        submit_form.click()
   
    def get_total_price(self):
         total_price = self._driver.find_element(
             By.CSS_SELECTOR, "div.summary_total_label").text
         return total_price 
   
   
    
    