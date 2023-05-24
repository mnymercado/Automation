from selenium.webdriver.common.by import By
from pages.main_page import Page


class SignInPage(Page):
    SIGNIN_BTN = (By.CSS_SELECTOR, 'a.nav-a[href*="https://www.amazon.com/ap/signin"]')
    SIGNIN_INPUT_FIELD = (By.ID, "ap_email")

    def open_signin_page(self):
        self.open_url('https://www.amazon.com')

    def signin_page_btn(self):
        self.click(*self.SIGNIN_BTN)

    def sign_email_input_field(self):
        self.input_text(*self.SIGNIN_INPUT_FIELD).send_keys()
