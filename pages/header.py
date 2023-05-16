from pages.base_page import Page
from selenium.webdriver.common.by import By
from features.steps import amazon_main_page_steps


class Header(Page):
    AMAZON_SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    NAV_LINKS = (By.CSS_SELECTOR, '#nav-xshop .nav-a')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_BTN)

    def ham_menu(self):
        self.find_element(*self.HAM_MENU)

    def click_ham_menu(self):
        self.click(*self.HAM_MENU)

    def no_of_header_link(self, *locator):
        pass

