from selenium.webdriver.common.by import By
from behave import given, when, then

from time import sleep

FOOTER_LINKS = (By.CSS_SELECTOR, 'table.navFooterMoreOnAmazon td.navFooterDescItem')
NAV_LINKS = (By.CSS_SELECTOR, '#nav-xshop .nav-a')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.implicitly_wait(10)
    context.app.main_page.open_main()


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.app.header.input_search_text(search_word)


@when('Click on search button')
def click_search(context):
    context.app.header.click_search()


@then('Verify that text {expected_res} is shown')
def verify_search_result(context, expected_res):
    context.app.search_results_page.verify_search_result(expected_res)


@then('Verify hamburger menu icon')
def verify_menu(context):
    context.app.header.ham_menu()


@when('Click on hamburger menu')
def click_hamburger_menu(context):
    context.app.header.click_ham_menu()


@then('Verify footer has {number_of_link} links')
def footer_links(context, number_of_link):
    # print('Original Type: ', type(number_of_link))
    # print('New Type: ', type(number_of_link))

    # print(footer_link)
    # print('Link No: ', len(footer_link))

    number_of_link = int(number_of_link)
    footer_link = context.driver.find_elements(*FOOTER_LINKS)
    assert len(footer_link) == number_of_link, f'Expected {number_of_link} links but got {len(footer_link)}'


@then('Verify header has {no_of_head_link} links')
def header_links(context, no_of_head_link):
    no_of_head_link = int(no_of_head_link)
    head_link = context.driver.find_elements(*NAV_LINKS)
    assert len(head_link) == no_of_head_link, f'Expected {no_of_head_link} links but got {len(head_link)}'

    context.app.header.no_of_header_link()

@when('Click Sign in Page button')
def click_signin_btn(context):
    context.app.signin_page_btn.signin_page_btn()


