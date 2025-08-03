import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
        )

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # Check 'Create course' page has the default state
        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title='', description='', estimated_time='', min_score='0', max_score='0'
        )
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        # Fill Course data and submit for adding
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Check created Course is in the list and with the proper data
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):

        # Step 1. Open course creation page
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # Step 2. Fill out the form with valid data, upload an image and save the course
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Step 3. Check if the created course card is displayed in the list of courses
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

        # Step 4. Open the created course card for editing
        courses_list_page.course_view.menu.click_edit(index=0)

        # Step 5. Modify fields (title, estimated time, description, max score, min score) and save the changes
        create_course_page.create_course_form.fill(
            title="Pytest",
            estimated_time="1 week",
            description="Pytest",
            max_score="1000",
            min_score="1"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # Step 6. Check if the course card with updated data is displayed
        courses_list_page.course_view.check_visible(
            index=0,
            title="Pytest",
            max_score="1000",
            min_score="1",
            estimated_time="1 week"
        )



