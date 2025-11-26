from selenium.webdriver.common.by import By

class AuthPage():
    def __init__(self, driver):
        self._driver = driver
    
    def open(self):
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()
        
    def get_login(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(term)
        
    def get_password(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(term)
        
    def submit_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    
        