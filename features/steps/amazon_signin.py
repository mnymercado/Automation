from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-signin-button span.nav-action-inner')


@given('Open Sign-In Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.driver.implicitly_wait(5)


@when('Click Returns and Orders')
def click_returns_and_orders_btn(context):
    context.driver.find_element(By.ID, "nav-orders").click()


@when('Input in input field {name}')
def input_text(context, name):
    context.driver.find_element(By.ID, "ap_email").send_keys(name)


@then('Verify amazon logo, continue button, Need help, Forgot Password, Other issues with Sign-In, Create you Amazon account button and {sign_in} text is shown')
def verify_signin(context, sign_in):
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert actual_result == sign_in, f'Expected {sign_in}, but {actual_result} is shown'
    assert context.driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']"), f'Amazon logo not shown' #Amazon Logo
    assert context.driver.find_element(By.ID, "continue"), f'Continue button not shown' #Continue button
    assert context.driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']"), f'Need Help not shown' # Need Help Link
    assert context.driver.find_element(By.ID, "auth-fpp-link-bottom"), f'Forgot password link not shown' # Forgot Password Link
    assert context.driver.find_element(By.ID, "ap-other-signin-issues-link"), f'Other issues in Signin link not found' # Other issues with Sign-In link
    assert context.driver.find_element(By.ID, "createAccountSubmit"), f'Create Amazon account button not shown' # Create your Amazon account button


@when('Click Cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'span.nav-cart-icon').click()


@then('Verify that {cart_status}')
def verify_cart(context, cart_status):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty').text
    assert actual_result == cart_status, f'Expected result is {cart_status}, but {actual_result} is shown'


@when('Click pop up Sign In page')
def click_popup_signin_page(context):
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BTN))
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGNIN_BTN),
        message='Sign in button not clickable'
    ).click()
    # context.driver.find_element(*SIGNIN_BTN).click()


@then('Verify {signin_text} Page is open')
def verify_signin_page_open(context, signin_text):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    signin = context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
    assert signin == signin_text, f'Sign in page not opened'


@then('Verify Sign in popup shown')
def click_popup_signin_page(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGNIN_BTN),
        message='Sign in button not clickable'
    )
    # context.driver.find_element(*SIGNIN_BTN).click()


@then('Wait for {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@then('Verify Signin popup disappears')
def verify_popup_disappears(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGNIN_BTN),
        message='Sign in button did not disappear'
    )
