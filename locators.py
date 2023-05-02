from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



service = Service('/Users/nicolemercado/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

# find element by ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# find element by XPATH

# By XPATH, tag & attribute
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")

# By XPATH, multiple attributes
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo' and @aria-label='Amazon']")

# By XPATH, contains (used to contain a long href or any value of attribute)
driver.find_element(By.XPATH, "//input[contains(@type, 'submit')]")

# By XPATH, without a tag name
driver.find_element(By.XPATH, "//*[contains(@href, '/b/?_encoding=UTF8&ld=AZUSSOA-sell&node=12766669011&ref_=nav_cs_sell')]") # with tag and attributes
driver.find_element(By.XPATH, "//*[contains (@href,'nav_cs_sell')]") #contains to make the url shorter
driver.find_element(By.XPATH, "//a[starts-with(@href, '/b/?_encoding=UTF8&ld=AZUSSOA')]") #starts-with to make the url shorter but it has to be the start url to copy

# By XPATH, connect with text
driver.find_element(By.XPATH, "//h2[text()='Gaming accessories']")

# By XPATH, from child up to parent
driver.find_element(By.XPATH, "//*[./a[contains(@href, '/customer-preferences/edit')][@id='icp-nav-flyout']]")


#1st Task
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']") # Amazon Logo
driver.find_element(By.ID, "ap_email") # Email Field
driver.find_element(By.ID, "continue") # Continue Field
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click() # Need Help Link
driver.find_element(By.ID, "auth-fpp-link-bottom") # Forgot Password Link
driver.find_element(By.ID, "ap-other-signin-issues-link") # Other issues with Sign-In link
driver.find_element(By.ID, "createAccountSubmit") # Create your Amazon account button
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']") # Conditions of use link
driver.find_element(By.XPATH, "//a[@href= '/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']") # Privacy Notice link


driver.quit()
