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
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, attachment_type.HTML, '.html')
    browser.quit()
