from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xvfbwrapper import Xvfb
import re
import pytest

@pytest.fixture(scope="session")
def w_driver(request):
    xvfb = Xvfb(width=1280, height=720)
    xvfb.start()
    driver=webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver

def test_navigates_to_kasner(w_driver):
    w_driver.get('localhost:8000')

    results=w_driver.page_source
    text_found=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    assert(text_found != None)

def test_search_google_results_contain_google(w_driver):
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('google' + Keys.RETURN)

    results=w_driver.page_source
    text_found=re.search(r'Google', results)

    assert text_found != None

def test_search_o_results_contain_google_and_yahoo(w_driver):
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('o' + Keys.RETURN)

    results=w_driver.page_source
    google_found=re.search(r'Google', results)
    yahoo_found=re.search(r'Yahoo', results)

    assert (google_found != None) or (yahoo_found != None)

def test_search_random_characters_results_are_None(w_driver):
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('!*(&$@' + Keys.RETURN)

    results=w_driver.page_source
    text_found=re.search(r'No results', results)

    assert text_found != None


