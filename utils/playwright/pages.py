from typing import Any, Generator

import allure
from _pytest.fixtures import SubRequest
from allure_commons.types import AttachmentType
from playwright.sync_api import Playwright, Page


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None
) -> Generator[Page, Any, None]:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state=storage_state, record_video_dir=f'./videos/{test_name}')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f'./tracing/{test_name}.zip')

    browser.close()

    allure.attach.file(source=f"./tracing/{test_name}.zip", name=f'trace_{test_name}', extension='zip')
    allure.attach.file(
        source=page.video.path(),
        name=f'video_{test_name}',
        attachment_type=AttachmentType.WEBM
    )