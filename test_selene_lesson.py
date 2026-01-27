import pytest
from selene import browser, be, have

@pytest.fixture
def open_wiki():
    browser.open('https://wikipedia.org')
    browser.element('[name="search"]').should(be.blank).type('хохлы').press_enter()

def test_browser(open_wiki):
    browser.element('html').should(have.text('Хохол'))

def test_element_text(open_wiki):
    browser.element('html').should(have.text('Содержание'))