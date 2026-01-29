import pytest
from selene import browser, be, have

@pytest.fixture
def open_wiki():
    browser.open('/')
    browser.element('[name="search"]').should(be.blank).type('хохлы').press_enter()

def test_browser(open_wiki):
    browser.element('html').should(have.text('Хохол'))

def test_element_text(open_wiki):
    browser.element('html').should(have.text('Содержание'))

def test_login(open_wiki):
    browser.element('[id="pt-login"]').click( )
    browser.element('[id="wpName1"]').type('qwerty')
    browser.element('[id="wpPassword1"]').type('132456')
    browser.element('[id="wpLoginAttempt"]').click()

def test_login_with_enter(open_wiki):
    browser.element('#pt-login').click()
    browser.element('[id="wpName1"]').type('qwerty')
    browser.element('[id="wpPassword1"]').type('132456').press_enter()

