from selenium import webdriver
from CalcPage import CalcPage
import allure

@allure.title("Тестирование работы калькулятора")
@allure.severity("Critical")
@allure.description("Тест проверяет корректность работы калькулятора с использованием отложенного времени в 45 секунд")
@allure.feature("Calculation")
def test_calc():
    """
    Проверяет, что калькулятор корректно считает
    выражение и возвращает нужный результат.
    """
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome()   
    with allure.step("Открыть страницу калькулятора"):
        calc_page = CalcPage(browser)
        calc_page.open()
    with allure.step("Установить задержку"):
        calc_page.delay_field() 
    with allure.step("Выполнить операцию сложения"):
        calc_page.calc_buttons()
    with allure.step("Получить результат и проверить его"):
        result = calc_page.get_result()
        assert result == "15", f"Ожидался результат 15, получено: {result}"
        
    with allure.step("Закрыть браузер"):
        browser.quit()