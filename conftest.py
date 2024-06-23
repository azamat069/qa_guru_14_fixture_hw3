import pytest
from selene import browser
@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    yield
    browser.quit()