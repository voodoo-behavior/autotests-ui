import allure
from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        with allure.step(f'Getting locator with "data-testid={locator}" at index "{nth}'):
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Clicking {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth=nth, **kwargs)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking {self.type_of} "{self.name}" is visible'):
            locator = self.get_locator(nth=nth, **kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking {self.type_of} "{self.name}" has text "{text}"'):
            locator = self.get_locator(nth=nth, **kwargs)
            expect(locator).to_have_text(text)

