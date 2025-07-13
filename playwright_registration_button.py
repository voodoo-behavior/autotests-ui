from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')

    # Check Registration button is disabled before all the required are filled in
    expect(registration_button).to_be_disabled()

    expect(registration_email_input).to_be_visible()
    registration_email_input.fill('user.name@gmail.com')

    expect(registration_username_input).to_be_visible()
    registration_username_input.fill('username')

    expect(registration_password_input).to_be_visible()
    registration_password_input.fill('password')

    # Check Registration button is enabled
    expect(registration_button).to_be_enabled()