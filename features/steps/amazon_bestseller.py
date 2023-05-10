from selenium.webdriver.common.by import By
from behave import given, when, then

BEST_SELLER_LINKS = (By.CSS_SELECTOR, 'div[class*="nav-tab-all_style_zg-tabs"] li')
NAV_TITLE = (By.ID, 'zg_banner_text') #HEADER
NAV_LINKS = (By.CSS_SELECTOR, 'div[class*="nav-tab-all_style_zg-tabs"] li') #TOP LINKS

@given('Open Amazon Bestseller Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.implicitly_wait(5)


@then('Verify Nav has {best_seller_links} links')
def nav_links(context, best_seller_links):
    best_seller_links = int(best_seller_links)
    nav_link = context.driver.find_elements(*BEST_SELLER_LINKS)
    # print(len(nav_link))
    assert len(nav_link) == best_seller_links, f'Expected {best_seller_links} links but got {len(nav_link)}'


@then('Verify each nav opens the right page')
def verify_each_nav(context):
    nav_link = context.driver.find_elements(*NAV_LINKS)

    print(len(nav_link))
    for i in range(len(nav_link)):

        link_to_click = context.driver.find_elements(*NAV_LINKS)[i]
        nav_title = link_to_click.text
        print(nav_title)

        link_to_click.click()

        nav_header_name = context.driver.find_element(*NAV_TITLE).text
        print(nav_header_name)
        assert nav_title in nav_header_name, f'Expected {nav_title} to be in {nav_header_name}'
