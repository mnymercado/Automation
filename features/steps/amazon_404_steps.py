from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

DOG_IMG = (By.CSS_SELECTOR, 'img#d')
@given('Store original window')
def store_current_window(context):
    context.current_window = context.driver.current_window_handle
    # print(context.current_window)

@when('Click on dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()
    sleep(5)


@when('Switch to new window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])

    print('All windows:', windows)
    # print('Last window: ', context.current_window)
    # print('Current window: ', windows[1])


@then('Verify blog is opened')
def verify_blog_opened(context):
    print('Current URL:', context.driver.current_url)
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/'))


@then('Close blog')
def close_blog(context):
    # windows = context.driver.window_handles
    # print('All windows:', windows)
    context.driver.close()


@then('Return to original window')
def return_orig_window(context):
    context.driver.switch_to.window(context.current_window)

