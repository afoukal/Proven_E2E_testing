from time import sleep

from behave import given, when, then


@given("Open Home page")
def open_home_page(context):
    context.app.base_page.open_page()


@when("Choose Get My Formula")
def click_get_my_formula(context):
    context.app.home_page.click_get_my_formula()


@then("Verify introductory message is displayed")
def introductory_message_is_visible(context):
    context.app.quiz_concern_page.introductory_message_is_visible()


@when("Introductory message disappear")
def introductory_message_disappear(context):
    context.app.quiz_concern_page.introductory_message_disappear()


@then('Concern question is displayed')
def concern_question_is_displayed(context):
    context.app.quiz_concern_page.concern_question_is_displayed()


@then("Concern question instruction is displayed")
def concern_instruction_text(context):
    context.app.quiz_concern_page.concern_instruction_text()


@then("All concern options are displayed")
def concern_option_text(context):
    context.app.quiz_concern_page.sensitivity_concern_text()
    context.app.quiz_concern_page.redness_concern_text()
    context.app.quiz_concern_page.wrinkles_concern_text()
    context.app.quiz_concern_page.firmness_loss_text()
    context.app.quiz_concern_page.hyperpigmentation_concern_text()
    context.app.quiz_concern_page.acne_concern_text()
    context.app.quiz_concern_page.dryness_concern_text()
    context.app.quiz_concern_page.other_concern_text()


@when('Choose Sensitivity and Redness concerns')
def sensitivity_redness_concern(context):
    context.app.quiz_concern_page.sensitivity_concern_click()
    context.app.quiz_concern_page.redness_concern_click()


@when('Click Next')
def click_next(context):
    context.app.quiz_concern_page.click_next()


@when('Provide User name {name}')
def name_input(context,name):
    context.app.quiz_concern_page.name_input(name)
    context.app.quiz_concern_page.click_next()


@given('Open Q1_sensitivity question')
def open_q1_sensitivity(context):
    context.app.base_page.open_page_additional("quiz/Q1_sensitivity")
    sleep(4)