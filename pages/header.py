from pages.base_page import Page
from selenium.webdriver.common.by import By
from features.steps import amazon_main_page_steps


class Header(Page):
    AMAZON_SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_BTN)
