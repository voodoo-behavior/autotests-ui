import pytest
from playwright.sync_api import expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):

    courses_list_page.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()


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


@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.parametrize("title, description, max_score, min_score, estimated_time, file_path", [
    (
            "Playwright",
            "Playwright",
            "100", "10",
            "2 weeks",
            "./testdata/files/image.png"
    )
])
def test_create_course(
        create_course_page: CreateCoursePage,
        courses_list_page: CoursesListPage,
        title: str,
        description: str,
        max_score: str,
        min_score: str,
        estimated_time: str,
        file_path: str
):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # Check 'Create course' page has the default state
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        '', '', '', '0', '0'
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    # Fill Course data and submit for adding
    create_course_page.upload_preview_image(file_path)
    create_course_page.check_visible_image_upload_view(True)
    create_course_page.fill_create_course_form(
        title,
        estimated_time,
        description,
        max_score,
        min_score
    )
    create_course_page.click_create_course_button()

    # Check created Course is in the list and with the proper data
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        0,
        title,
        max_score,
        min_score,
        estimated_time
    )
