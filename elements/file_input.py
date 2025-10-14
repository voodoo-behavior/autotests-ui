import allure

from elements.base_element import BaseElement
from utils.logger import get_logger
logger = get_logger("FILE_INPUT")


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return 'file input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        step = f'Setting file "{file}" to {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth=nth, **kwargs)
            logger.info(step)
            locator.set_input_files(file)