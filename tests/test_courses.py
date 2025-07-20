import pytest
from playwright.sync_api import expect, Page

from fixtures.browsers import chromium_page_without_state
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


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
        ("user.name@gmail.com", '  '),
        ('  ', "password")
])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.fill_login_form(email, password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

@pytest.mark.parametrize("email, username, password", [
        ("user.name@gmail.com", "username", "password")
])
def test_successful_registration(
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
        email: str,
        username: str,
        password: str
):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.fill_registration_form(email, username, password)
        registration_page.click_registration_button()
        dashboard_page.check_visible_dashboard_title()