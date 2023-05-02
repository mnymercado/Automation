from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON_SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(5)

@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_INPUT).send_keys(search_word)

@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_BTN).click()

@then('Verify that text {expected_res} is shown')
def verify_search_result(context, expected_res):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert actual_result == expected_res, f'Expected {expected_res}, but it shows {actual_result}'
