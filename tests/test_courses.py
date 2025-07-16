import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
        courses_list = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")

        expect(courses_title).to_contain_text("Courses")
        expect(courses_title).to_be_visible()

        expect(courses_list).to_have_text("There is no results")
        expect(courses_list).to_be_visible()

@pytest.mark.parametrize("email, password", [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
])
def test_wrong_email_or_password_authorization(chromium_page_without_state: Page, email: str, password: str):

        chromium_page_without_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = chromium_page_without_state.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill(email)

        password_input = chromium_page_without_state.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill(password)

        login_button = chromium_page_without_state.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_email_or_password_alert = chromium_page_without_state.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
        chromium_page_without_state.wait_for_timeout(2000)