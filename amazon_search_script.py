from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


service = Service('/Users/nicolemercado/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

sleep(15)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('phone')
driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"phone"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert actual_result == expected_result, f'Expected {expected_result}, but it shows {actual_result}'
print("Test Passed")

sleep(3)
driver.quit()

