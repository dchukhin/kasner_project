from selenium import webdriver
from selenium. webdriver.common.keys import Keys
import re

browser=webdriver.Firefox()

def test_navigates_to_kasner():
    browser.get('localhost:8000')

    results=browser.page_source
    text_found=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    assert(text_found != None)

def test_search_google_results_contain_google():
    browser.get('localhost:8000')
    element = browser.find_element_by_name('query')
    element.send_keys('google' + Keys.RETURN)

    results=browser.page_source
    text_found=re.search(r'Google', results)

    assert text_found != None

def test_search_o_results_contain_google_and_yahoo():
    browser.get('localhost:8000')
    element = browser.find_element_by_name('query')
    element.send_keys('o' + Keys.RETURN)

    results=browser.page_source
    google_found=re.search(r'Google', results)
    yahoo_found=re.search(r'Yahoo', results)

    assert (google_found != None) or (yahoo_found != None)

def test_search_random_characters_results_are_None():
    browser.get('localhost:8000')
    element = browser.find_element_by_name('query')
    element.send_keys('!*(&$@' + Keys.RETURN)

    results=browser.page_source
    text_found=re.search(r'No results', results)

    assert text_found != None

    browser.quit()

