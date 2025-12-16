from selenium.webdriver.common.by import By
import allure

class AuthPage():
    def __init__(self, driver) -> None:
        """
        Инициализация страницы авторизации.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        
    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации и увеличивает окно браузера.
        """
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()
        
    @allure.step("Ввести username {term}")  
    def get_login(self, term) -> None:
        """
        Вводит заданный логин в поле 'username'.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(term)
        
    @allure.step("Ввести password {term}")  
    def get_password(self, term) -> None:
        """
        Вводит заданный пароль в поле 'password'.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(term)
        
    @allure.step("Нажать кнопку 'login'")      
    def submit_button(self) -> None:
        """
        Переходит на страницу магазина,
        после нажатия на кнопку 'login' и подтверждения авторизации.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    