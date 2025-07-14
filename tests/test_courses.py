import pytest
from playwright.sync_api import expect, Page


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