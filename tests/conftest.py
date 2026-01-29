
import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = 'https://ru.wikipedia.org/'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options

    yield

    browser.quit()