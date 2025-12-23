from selenium import webdriver
from CalcPage import CalcPage

def test_calc():
    browser = webdriver.Chrome()
    calc_page = CalcPage(browser)
    calc_page.open()
    calc_page.delay_field() 
    calc_page.calc_buttons()
    result = calc_page.get_result()
    assert result == "15", f"Ожидался результат 15, получено: {result}"

    browser.quit()