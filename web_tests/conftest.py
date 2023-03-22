import pytest
from selene.support.shared import browser
from demoqa_tests.utils import attach


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    browser.quit()
