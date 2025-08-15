from typing import Any, Generator

import allure
from _pytest.fixtures import SubRequest
from allure_commons.types import AttachmentType
from playwright.sync_api import Playwright, Page
from config import settings


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None
) -> Generator[Page, Any, None]:

    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir.joinpath(f'{test_name}')
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()

    allure.attach.file(
        source=settings.tracing_dir.joinpath(f'{test_name}.zip'),
        name=f'trace_{test_name}.zip',
        extension='zip'
    )
    allure.attach.file(
        source=page.video.path(),
        name=f'video_{test_name}',
        attachment_type=AttachmentType.WEBM
    )