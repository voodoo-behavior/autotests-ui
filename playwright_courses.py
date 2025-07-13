from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
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


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="storage_state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    coursesTitle = page.get_by_test_id("courses-list-toolbar-title-text")
    coursesList = page.get_by_test_id("courses-list-empty-view-title-text")

    expect(coursesTitle).to_contain_text("Courses")
    expect(coursesTitle).to_be_visible()

    expect(coursesList).to_have_text("There is no results")
    expect(coursesList).to_be_visible()

