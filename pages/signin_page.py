from selenium.webdriver.common.by import By
from pages.main_page import Page


class SignInPage(Page):
    SIGNIN_BTN = (By.CSS_SELECTOR, 'a.nav-a[href*="https://www.amazon.com/ap/signin"]')

    def signin_page_btn(self):
        self.click(*self.SIGNIN_BTN)
