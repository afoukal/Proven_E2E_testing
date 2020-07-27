from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QuizConcernPage(BasePage):
    INTRODUCTORY_MESSAGE = (By.CSS_SELECTOR, ".src-components-quiz-transition-___transition__transition___1JiNQ h4")
    NEXT_BTN = (By.CSS_SELECTOR, ".src-components-quiz-navigation-___navigation__navigation___sA9jk>button")
    CONCERN_QUESTION = (By.CSS_SELECTOR, ".src-components-quiz-question-question-header-___question-header__question-title___3aolS div")
    CONCERN_INSTRUCTION = (By.CSS_SELECTOR, ".src-components-quiz-question-question-hint-___question-hint__question-hint___2nAKl")
    CONCERN_SENSITIVITY = (By.XPATH, "//*[@id='Sensitivity']/parent::*")
    CONCERN_REDNESS = (By.XPATH, "//*[@id='Redness']/parent::*")
    CONCERN_WRINKLES = (By.XPATH, "//*[@id='Fine lines or wrinkles']/parent::*")
    CONCERN_FIRMNESS_LOSS = (By.XPATH, "//*[@id='Loss of firmness or elasticity']/parent::*")
    CONCERN_HYPERPIGMENTATION = (By.XPATH, "//*[@id='Hyperpigmentation']/parent::*")
    CONCERN_ACNE = (By.XPATH, "//*[@id='Acne']/parent::*")
    CONCERN_DRYNESS = (By.XPATH, "//*[@id='Dryness']/parent::*")
    CONCERN_OTHER = (By.XPATH, "//*[@id='Other']/parent::*")
    YOUR_NAME = (By.CSS_SELECTOR, ".src-components-shared-input-___input__input___19sfG")

    def introductory_message_is_visible(self):
        self.verify_text("3 minutes to your best skincare, let's go!", *self.INTRODUCTORY_MESSAGE)

    def introductory_message_disappear(self):
        self.wait_for_element_disappear(*self.INTRODUCTORY_MESSAGE)

    def concern_question_is_displayed(self):
        self.verify_text("What are your main skin concerns?", *self.CONCERN_QUESTION)

    def concern_instruction_text(self):
        self.verify_text("Choose all that apply", *self.CONCERN_INSTRUCTION)

    def sensitivity_concern_text(self):
        self.verify_text("Sensitivity", *self.CONCERN_SENSITIVITY)

    def redness_concern_text(self):
        self.verify_text("Redness", *self.CONCERN_REDNESS)

    def wrinkles_concern_text(self):
        self.verify_text("Fine lines or wrinkles", *self.CONCERN_WRINKLES)

    def firmness_loss_text(self):
        self.verify_text("Loss of firmness or elasticity", *self.CONCERN_FIRMNESS_LOSS)

    def hyperpigmentation_concern_text(self):
        self.verify_text("Hyperpigmentation", *self.CONCERN_HYPERPIGMENTATION)

    def acne_concern_text(self):
        self.verify_text("Acne", *self.CONCERN_ACNE)

    def dryness_concern_text(self):
        self.verify_text("Dryness", *self.CONCERN_DRYNESS)

    def other_concern_text(self):
        self.verify_text("Other", *self.CONCERN_OTHER)

    def sensitivity_concern_click(self):
        self.click(*self.CONCERN_SENSITIVITY)

    def redness_concern_click(self):
        self.click(*self.CONCERN_REDNESS)

    def wrinkles_concern_click(self):
        self.click(*self.CONCERN_WRINKLES)

    def firmness_loss_click(self):
        self.click(*self.CONCERN_FIRMNESS_LOSS)

    def hyperpigmentation_concern_click(self):
        self.click(*self.CONCERN_HYPERPIGMENTATION)

    def acne_concern_click(self):
        self.click(*self.CONCERN_ACNE)

    def dryness_concern_click(self):
        self.click(*self.CONCERN_DRYNESS)

    def other_concern_click(self):
        self.click(*self.CONCERN_OTHER)

    def name_input(self, name):
        self.input(name, *self.YOUR_NAME)

    def click_next(self):
        self.click(*self.NEXT_BTN)