from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON_SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td.navFooterDescItem')
NAV_LINKS = (By.CSS_SELECTOR, '#nav-xshop .nav-a')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.driver.implicitly_wait(5)

@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(*AMAZON_SEARCH_INPUT).send_keys(search_word)
    context.product_name = search_word
@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_BTN).click()

@then('Verify that text {expected_res} is shown')
def verify_search_result(context, expected_res):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert actual_result == expected_res, f'Expected {expected_res}, but it shows {actual_result}'

@then('Verify hamburger menu icon')
def verify_menu(context):
    element = context.driver.find_element(*HAM_MENU)
    print(element)

@then('Verify footer has {number_of_link} links')
def footer_links(context, number_of_link):
    # print('Original Type: ', type(number_of_link))
    number_of_link = int(number_of_link)
    # print('New Type: ', type(number_of_link))
    footer_link = context.driver.find_elements(*FOOTER_LINKS)
    # print(footer_link)
    # print('Link No: ', len(footer_link))
    assert len(footer_link) == number_of_link, f'Expected {number_of_link} links but got {len(footer_link)}'


@then('Verify header has {no_of_head_link} links')
def header_links(context, no_of_head_link):
    no_of_head_link = int(no_of_head_link)
    head_link = context.driver.find_elements(*NAV_LINKS)
    assert len(head_link) == no_of_head_link, f'Expected {no_of_head_link} links but got {len(head_link)}'