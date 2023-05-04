from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

CUSTSERVICE_PAGE = (By.CSS_SELECTOR, 'a.nav-a[data-csa-c-content-id="nav_cs_customerservice"]')
WELCOMECUST_DIV = (By.CSS_SELECTOR, 'div.issue-card-container div.issue-card-wrapper')
WELCOMECUST_INPUT_FIELD = (By.ID, 'hubHelpSearchInput')
NUM_OF_TOPICS = (By.CSS_SELECTOR, 'li.help-topics')


@when('Go to Customer Service Page')
def customer_service_page(context):
    context.driver.find_element(*CUSTSERVICE_PAGE).click()
    # sleep(3)



@when('Verify text {expected_res} is shown')
def welcome_amazon_custS(context, expected_res):
    welcome = context.driver.find_element(By.CSS_SELECTOR, 'h1.fs-heading').text
    # print('Actual res:', welcome, 'Expected:', expected_res)
    assert expected_res == welcome, f'Expected {expected_res}, but {welcome} is shown'  # Verify Amazon Customer Service text shown


@then('Verify {number_of_div} div is shown')
def verify_cust_div(context, number_of_div):
    actual_no_div = context.driver.find_elements(*WELCOMECUST_DIV)
    number_of_div = int(number_of_div)
    # print('Actual:', len(actual_no_div), 'Set is:', number_of_div)
    assert len(actual_no_div) == number_of_div, f'Expected no is {number_of_div}, but no is {len(actual_no_div)}'


@then('Verify the Search our help library, All help topics is present and input field is present')
def verify_all_help_and_reco_topics(context):
    all_topic_lbl = context.driver.find_elements(By.CSS_SELECTOR, 'h2.fs-heading.bolded'), f'Search our help library and All help topics are not shown'
    assert len(all_topic_lbl) == 2, f'Length of All help topics and help library now shown'
    assert context.driver.find_element(*WELCOMECUST_INPUT_FIELD), f'Input field not present'  # Input field after Search library label


@then('Verify {number_of_topics} Search help topics')
def help_topics(context, number_of_topics):
    no_of_topics = context.driver.find_elements(*NUM_OF_TOPICS)
    number_of_topics = int(number_of_topics)
    # print(len(no_of_topics))
    assert len(no_of_topics) == number_of_topics, f'No. of topics is {number_of_topics}, but no is {len(no_of_topics)}'
