import pytest
from selene.support.shared import browser
from selene import command, have
from allure import attachment_type
import allure


@pytest.fixture(autouse=True)
def open_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    allure.attach(browser.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=attachment_type.JPG)
    allure.attach(browser.driver.page_source, name='Page Source', attachment_type=attachment_type.HTML)
    allure.attach(("".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))), name='Log',
                  attachment_type=attachment_type.TEXT)
    browser.quit()
