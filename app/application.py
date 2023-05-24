from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SignInPage
from pages.cart_main_page import Cart


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.signin_page_btn = SignInPage(self.driver)
        self.cart_main_page = Cart(self.driver)
        self.open_signin_page = SignInPage(self.driver)
