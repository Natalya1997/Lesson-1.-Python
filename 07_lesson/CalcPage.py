from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage():
    def __init__(self, driver):
        self._driver = driver
        
    def open(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()
     
    def delay_field(self):
        delay_input = WebDriverWait(self._driver, 20).until(
        EC.visibility_of_element_located((By.ID, "delay")))                             
        delay_input.clear()                                                                 
        delay_input.send_keys("45")                                                       
    
    def calc_buttons(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
        
    def get_result(self):
        WebDriverWait(self._driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))               

        self.result = self._driver.find_element(By.CLASS_NAME, "screen").text                      
        assert self.result == "15", f"Ожидался результат 15, получено: {self.result}"                  

