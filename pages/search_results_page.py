from selenium.webdriver.common.by import By
from pages.main_page import Page


class SearchResultsPage(Page):
    ACTUAL_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def verify_search_result(self, expected_result):
        # actual_result = self.driver.find_element(*self.ACTUAL_RESULT).text
        # assert actual_result == expected_result, f'Expected {expected_result}, but it shows {actual_result}'
        self.verify_text(expected_result, *self.ACTUAL_RESULT)
