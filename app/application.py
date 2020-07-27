from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.quiz_concern_page import QuizConcernPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.quiz_concern_page = QuizConcernPage(self.driver)