from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

T_AND_C_LINK = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')
PRIVACY_TEXT = (By.ID, 'GUID-8966E75F-9B92-4A2B-BFD5-967D57513A40__GUID-2C1DF364-8FA3-4387-BCDB-2A63B7C51B64')


@given('Open Amazon T&C page')
def open_terms_and_conditions(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
    # sleep(5)


@when('Store original windows')
def tc_original_window(context):
    context.original_window = context.driver.current_window_handle
    # print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*T_AND_C_LINK).click()
    # sleep(5)


@when('Switch to the newly opened window')
def switch_to_tec(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])

    print('All windows:', windows)
    print('Current window: ', windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_is_open(context):
    privacy_text = context.driver.find_element(*PRIVACY_TEXT).text
    # print(privacy_text)
    assert 'Amazon.com Privacy Notice' in privacy_text, f'Expected text: Amazon.com Privacy Notice but {privacy_text}'


@then('User can close new window and switch back to original')
def switch_original_window(context):
    context.driver.switch_to.window(context.original_window)
    print(context.original_window)
