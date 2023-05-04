from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_RESULT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
PRODUCT_NAME = (By.CSS_SELECTOR, 'li.a-spacing-mini a.sc-product-link')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')

@when('Click first product')
def click_first_prod(context):
    context.driver.find_element(*SEARCH_RESULT_PRICE).click()
    sleep(2)

@when('Click Add to Cart button')
def open_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()

@when('Go to Amazon Cart')
def go_to_amazon_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/cart?ref_=sw_gtc"]').click()

@then('Verify cart not empty')
def cart_not_empty(context):
    assert context.driver.find_element(By.ID, 'activeCartViewForm'), f'Cart is empty'

@then('Verify cart has correct item')
def cart_correct_prod(context):
    prod_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Cart Product Name: {prod_name}')
    print(f'Searched name: {context.product_name}')
    assert context.product_name in prod_name[:50], f'Not the right product'
