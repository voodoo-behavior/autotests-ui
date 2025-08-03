import allure
from playwright.sync_api import expect, Locator

from elements.base_element import BaseElement


class TextArea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'textarea'

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth=nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth:int = 0, **kwargs):
        with allure.step(f'Filling {self.type_of} "{self.name}" with "{value}"'):
            locator = self.get_locator(nth=nth, **kwargs)
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Checking {self.type_of} "{self.name}" has value "{value}"'):
            locator = self.get_locator(nth=nth, **kwargs)
            expect(locator).to_have_value(value)