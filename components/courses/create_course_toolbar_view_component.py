import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(
            page, 'create-course-toolbar-create-course-button', 'Create course button')

    @allure.step('Checking create course toolbar view is visible')
    def check_visible(self, is_create_course_disabled=True):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        if not is_create_course_disabled:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()