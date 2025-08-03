import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...
    with allure.step("Start browser"):
        ...

@allure.step("Creating course with title: '{title}'")
def create_course(title: str):
    ...

def close_browser(title: str):
    ...

def test_feature():
    open_browser()

    create_course("Test Course")

    with allure.step('Closing browser'):
        ...