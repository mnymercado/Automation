from pages.base_page import Page
from selenium.webdriver.common.by import By


class Cart(Page):

    CART_EMPTY_STATUS = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')

    def cart_status(self, cart_stat):

        actual_result = self.find_element(*self.CART_EMPTY_STATUS).text
        assert actual_result == cart_stat, f'Expected result is {cart_stat}, but {actual_result} is shown'


