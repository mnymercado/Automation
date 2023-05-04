from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BEST_SELLER_LINKS = (By.CSS_SELECTOR, 'div[class*="nav-tab-all_style_zg-tabs"] li')

@given('Open Amazon Bestseller Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    sleep(5)

@then('Verify Nav has {best_seller_links} links')
def nav_links(context, best_seller_links):
    best_seller_links = int(best_seller_links)
    nav_link = context.driver.find_elements(*BEST_SELLER_LINKS)
    assert len(nav_link) == best_seller_links, f'Expected {best_seller_links} links but got {len(nav_link)}'

