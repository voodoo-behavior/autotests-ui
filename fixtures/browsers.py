from typing import Any, Generator

import allure
from allure_commons.types import AttachmentType
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from pages.authentication.registration_page import RegistrationPage
from utils.playwright.pages import initialize_playwright_page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(
        email='user.name@gmail.com',
        username='username',
        password='password'
    )
    registration_page.click_registration_button()

    context.storage_state(path="storage_state.json")

    browser.close()


@pytest.fixture
def chromium_page_with_state(
        request: SubRequest, initialize_browser_state, playwright: Playwright) -> Generator[Page, Any, None]:
    yield from initialize_playwright_page(
        test_name=request.node.name,
        playwright=playwright,
        storage_state='storage_state.json'
    )


@pytest.fixture
def chromium_page_without_state(request: SubRequest, playwright: Playwright) -> Generator[Page, Any, None]:
    yield from initialize_playwright_page(
        test_name=request.node.name,
        playwright=playwright
    )
