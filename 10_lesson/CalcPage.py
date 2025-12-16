from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalcPage():
    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        
    @allure.step("Открыть страницу калькулятора")   
    def open(self) -> None:
        """
        Открывает страницу калькулятора и увеличивает окно браузера.
        """
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()
    
    @allure.step("Установить задержку 45 секунд")   
    def delay_field(self) -> None:
        """
        Удаляет предыдущее значение, и устанавливает задержку вычисления в 45 секунд.
        """
        delay_input = WebDriverWait(self._driver, 20).until(
        EC.visibility_of_element_located((By.ID, "delay")))                             
        delay_input.clear()                                                                 
        delay_input.send_keys("45")                                                       
    
    @allure.step("Нажать на кнопки калькулятора")  
    def calc_buttons(self) -> None:
        """
        Выполняет вычисление 7 + 8.
        """
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    @allure.step("Получить результат с экрана калькулятора")      
    def get_result(self) -> str:
        """
        Возвращает результат вычислений с экрана калькулятора.
        :return: результат вычислений в виде строки.
        """
        WebDriverWait(self._driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))               

        result = self._driver.find_element(By.CLASS_NAME, "screen").text   
        return result                   