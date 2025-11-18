from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

field = driver.find_element(By.CSS_SELECTOR, "input")
field.send_keys("Sky")
field.clear()
field.send_keys("Pro")

driver.quit()