from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


service = Service('/Users/nicolemercado/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

#By CSS, using tag#id
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

#By CSS, using tag.class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag')
#By CSS, using .class
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag')
#By CSS, using multiple class
driver.find_element(By.CSS_SELECTOR, 'header.nav-opt-sprite.nav-locale-us.nav-lang-en')

#By CSS, using tag[attribute=value] >>>>> Except ID and CLASS
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/goldbox?ref_=nav_cs_gb']")
#Multiple attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/goldbox?ref_=nav_cs_gb'][data-csa-c-type='link']")

#Class with attributes
driver.find_element(By.CSS_SELECTOR, "a.nav-a[href='/gp/goldbox?ref_=nav_cs_gb'][data-csa-c-type='link'][data-csa-c-slot-id='nav_cs_0']")
#Using contains in an href, just add *=
driver.find_element(By.CSS_SELECTOR, "a.nav-a[href*='/gp/goldbox']")

#By CSS, from parent to child
driver.find_element(By.CSS_SELECTOR, "header.nav-opt-sprite #navbar #nav-tools a[href*='/customer-preferences/']")



#-----------CSS LOCATORS TASK-------------
driver.find_element(By.ID, "nav-link-accountList").click()
driver.find_element(By.ID, "createAccountSubmit").click()
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
driver.find_element(By.ID, "ap_customer_name").send_keys('Nicole')
driver.find_element(By.ID, "ap_email").send_keys('mnymercado11@gmail.com')
driver.find_element(By.ID, "ap_password").send_keys('testpass')
driver.find_element(By.ID, "ap_password_check").send_keys('testpass')
driver.find_element(By.ID, "continue")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href*='/ap/signin']")

sleep(5)
expected_result = 'Create account'
actual_result = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
assert expected_result == actual_result, f'Expected result is {expected_result} but result is {actual_result}'
print('Test Passed')


driver.quit()