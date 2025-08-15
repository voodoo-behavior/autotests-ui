from playwright.sync_api import sync_playwright, expect

from config import settings
from utils.routes import AppRoute

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(base_url=settings.get_base_url())

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

    page.wait_for_url(AppRoute.DASHBOARD)
    page.wait_for_load_state("networkidle")

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_contain_text("Dashboard")
    expect(dashboard_title).to_be_visible()