from playwright.sync_api import sync_playwright, expect

from config import settings
from utils.routes import AppRoute

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')

    expect(registration_email_input).to_be_visible()
    registration_email_input.fill(settings.test_user.email)

    expect(registration_username_input).to_be_visible()
    registration_username_input.fill(settings.test_user.username)

    expect(registration_password_input).to_be_visible()
    registration_password_input.fill(settings.test_user.password)

    expect(registration_button).to_be_visible()
    registration_button.click()

    context.storage_state(path="storage_state.json")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="storage_state.json", base_url=settings.get_base_url())
    page = context.new_page()

    page.goto(AppRoute.COURSES)

    coursesTitle = page.get_by_test_id("courses-list-toolbar-title-text")
    coursesList = page.get_by_test_id("courses-list-empty-view-title-text")

    expect(coursesTitle).to_contain_text("Courses")
    expect(coursesTitle).to_be_visible()

    expect(coursesList).to_have_text("There is no results")
    expect(coursesList).to_be_visible()

