import pytest
from selene import browser


@pytest.fixture(autouse=True )
def browser_management():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 1280
    browser.config.window_width = 1280
    yield
    browser.quit()