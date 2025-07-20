import pytest
from playwright.sync_api import Page

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def login_page(chromium_page_without_state: Page) -> LoginPage:
    return LoginPage(page=chromium_page_without_state)

@pytest.fixture
def registration_page(chromium_page_without_state: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page_without_state)

@pytest.fixture
def dashboard_page(chromium_page_without_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_without_state)