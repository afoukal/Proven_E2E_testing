from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    GET_MY_FORMULA_BTN = (By.CSS_SELECTOR, ".src-components-shared-proven-button-___style__text___3aBIJ")

    def click_get_my_formula(self):
        self.find_element(*self.GET_MY_FORMULA_BTN).click()
