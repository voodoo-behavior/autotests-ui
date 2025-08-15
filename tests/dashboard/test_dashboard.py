import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.routes import AppRoute


@pytest.mark.regression
@pytest.mark.dashboard
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):

        dashboard_page_with_state.visit(AppRoute.DASHBOARD)

        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.sidebar.check_visible()

        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.scores_chart_view.check_visible('Scores')
        dashboard_page_with_state.students_chart_view.check_visible('Students')
        dashboard_page_with_state.courses_chart_view.check_visible('Courses')
        dashboard_page_with_state.activities_chart_view.check_visible('Activities')