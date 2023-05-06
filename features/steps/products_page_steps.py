from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


SEARCH_RESULT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
PRODUCT_NAME = (By.CSS_SELECTOR, 'li.a-spacing-mini a.sc-product-link')
COLOR_OPTIONS = (By.CSS_SELECTOR, 'span.a-list-item span[id*="color_name_"].a-button.a-button-toggle.image-swatch-button')
CURRENT_COLOR = (By.ID, 'inline-twister-expanded-dimension-text-color_name')
PRODUCT_RESULTS = (By.CSS_SELECTOR, 'div[cel_widget_id*="MAIN-SEARCH_RESULTS"]')

@when('Click first product')
def click_first_prod(context):
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_RESULT_PRICE))
    context.driver.find_element(*SEARCH_RESULT_PRICE).click()

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


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/Hanes-Sleeve-Jersey-Pocket-X-Large/dp/{product_id}')
    context.driver.implicitly_wait(10)

@then('Verify user can click through colors')
def verify_prod_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click()

    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy', 'Caramel', 'Dark Blue', 'Denim Blue', 'Gray', 'Green', 'Khaki', 'Light-green', 'Orange', 'Pink', 'Purple']
    actual_colors = []

    for color in color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        # print('Current color: ', current_color)
        actual_colors.append(current_color)

    # print('Actual color: ', actual_colors)

    assert expected_colors == actual_colors, f'Expected color is {expected_colors} but color is {actual_colors}'


@then('Verify user can clicks through specified color')
def verify_colors(context):
    #WAIT UNTIL THE ELEMENT IS CLICKABLE
    context.driver.wait.until(EC.element_to_be_clickable(COLOR_OPTIONS))
    #CLICK ELEMENT
    context.driver.find_element(*COLOR_OPTIONS).click()

    expected_colors = ['Light Wash', 'Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Khaki Brown', 'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Khaki Brown', 'Medium Blue, Vintage', 'Medium Wash', 'Olive', 'Rinsed']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)

    actual_colors = []

    for color in color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        # print('Current color: ', current_color)
        actual_colors.append(current_color)

    print('Actual color: ', actual_colors)
    print('Expected color: ', expected_colors)
    assert actual_colors == expected_colors, f'Expected color is {expected_colors} but color is {actual_colors}'


# $$('div[cel_widget_id*="MAIN-SEARCH_RESULTS"]') #Search_Results

@then('Verify image and title is present')
def verify_img_and_title(context):
    search_result = context.driver.find_elements(*PRODUCT_RESULTS)
    # img_result = context.driver.find_element(By.CSS_SELECTOR, 'div[cel_widget_id*="MAIN-SEARCH_RESULTS"] img[data-image-latency="s-product-image"]')
    # title_result = context.driver.find_element(By.CSS_SELECTOR, 'span.a-size-base-plus').text


    for result in search_result:
        # print(result)
        assert result.find_element(By.CSS_SELECTOR, 'img[data-image-latency="s-product-image"]'), 'No product image'
        assert result.find_element(By.CSS_SELECTOR, 'span.a-size-base-plus'), 'No product title'
        # print(result.find_element(By.CSS_SELECTOR, 'span.a-size-base-plus').text)
