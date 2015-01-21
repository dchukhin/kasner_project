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

def test_search_google(w_driver):
    """Tests whether searching for google will resurn google.com as a result"""
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('google' + Keys.RETURN)

    results=w_driver.page_source
    text_found=re.search(r'Google', results)

    assert text_found != None

def test_search_o_results_do_not_contain_google_and_yahoo(w_driver):
    """Tests whether searching for 'o' yields google and yahoo in results"""
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('o' + Keys.RETURN)

    results=w_driver.page_source
    google_found=re.search(r'Google', results)
    yahoo_found=re.search(r'Yahoo', results)

    assert (google_found == None) or (yahoo_found == None)

def test_search_random_characters(w_driver):
    """Tests whether searching for random characters fails to yield matches"""
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('!*(&$@' + Keys.RETURN)

    results=w_driver.page_source
    text_found=re.search(r'No results', results)

    assert text_found != None

@pytest.mark.whataaa
def test_search_case_insensitive(w_driver):
    """Tests whether case insensitive search yields correct results.
    
    1.) Search for 'yahoo', find 'Yahoo' in results
    2.) Search for Yahoo, find 'Yahoo' in results
    3.) Confirm that results of #1 and #2 are the same
    """
    w_driver.get('localhost:8000')
    import pdb
    pdb.set_trace()
    element = w_driver.find_element_by_name('query')
    element.send_keys('yahoo' + Keys.RETURN)
    results1=w_driver.page_source
    text_found1=re.search(r'Yahoo', results1)
    
    element = w_driver.find_element_by_name('query')
    element.send_keys('Yahoo' + Keys.RETURN)
    results2=w_driver.page_source
    text_found2=re.search(r'Yahoo', results2)

    assert results1 != results2

def test_search_keyword(w_driver):
    """Tests whether a search for a keyword yields results with that keyword.
            
    1.) Search for 'yahoo', find 'Yahoo' in results
    2.) Search for Yahoo, find 'Yahoo' in results
    3.) Confirm that results of #1 and #2 are not the same
    """
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('yahoo' + Keys.RETURN)
    results1=w_driver.page_source

    element = w_driver.find_element_by_name('query')
    element.send_keys('Yahoo' + Keys.RETURN)
    results2=w_driver.page_source

    assert text_found1 == text_found2


