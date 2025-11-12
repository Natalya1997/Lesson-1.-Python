from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("Skypro")
new_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
new_button.click()

print(new_button.text)

driver.quit()


