from typing import Any, Generator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, expect, Page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_button = page.get_by_test_id('registration-page-registration-button')

        expect(registration_email_input).to_be_visible()
        registration_email_input.fill('user.name@gmail.com')

        expect(registration_username_input).to_be_visible()
        registration_username_input.fill('username')

        expect(registration_password_input).to_be_visible()
        registration_password_input.fill('password')

        expect(registration_button).to_be_visible()
        registration_button.click()

        context.storage_state(path="storage_state.json")

        browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Generator[Page, Any, None]:
    # Pycharm suggests using Generator[Page, Any, None] instead of Page for yield statement
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="storage_state.json")
    yield context.new_page()
    browser.close()

@pytest.fixture
def chromium_page_without_state(playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context.new_page()
    browser.close()
