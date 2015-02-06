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

#for a few tests we use Chrome instead of Firefox
@pytest.fixture(scope="session")
def chrome_driver(request):
    xvfb = Xvfb(width=1280, height=720)
    xvfb.start()
    driver=webdriver.Chrome('/usr/bin/chromedriver')
    request.addfinalizer(driver.quit)
    return driver

@pytest.mark.new
def test_correct_css_file_loads(w_driver, chrome_driver):
    """
    Tests whether the correct CSS loads for a single page.
    The CSS loaded for the page should match the browser. So, for Mozilla
    Firefox the CSS loaded should end in firefox.css, for Google Chrome it
    should end in chrome.css, and so on.
    Test verifies that
    1.) for Firefox:
    a) index page loads a css file that ends in firefox.css
    b) about page loads a css file that ends in firefox.css
    c) results page loads a css file that ends in firefox.css
    d) an empty search returns a page with a css file ending in firefox.css
    2.) for Chrome:
    a) index page loads a css file that ends in chrome.css
    b) about page loads a css file that ends in chrome.css
    c) results page loads a css file that ends in chrome.css
    d) an empty search returns a page with a css file ending in chrome.css
    """
    #1.) for Firefox:
    #a) index page loads a css file that ends in firefox.css
    w_driver.get('localhost:8000')
    results=w_driver.page_source
    css_found=re.search(r'firefox.css',results)
    assert (css_found != None)

    #b) about page loads a css file that ends in firefox.css
    w_driver.get('localhost:8000/about')
    results=w_driver.page_source
    css_found=re.search(r'firefox.css',results)
    assert (css_found != None)

    #c) results page loads a css file that ends in firefox.css
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('testing' + Keys.RETURN)
    results=w_driver.page_source
    css_found=re.search(r'firefox.css',results)
    assert (css_found != None)

    #d) an empty search returns a page with a css file ending in firefox.css
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('' + Keys.RETURN)
    results=w_driver.page_source
    css_found=re.search(r'firefox.css',results)
    assert (css_found != None)

    #2.) for Chrome:
    #a) index page loads a css file that ends in chrome.css
    chrome_driver.get('localhost:8000')
    results=chrome_driver.page_source
    css_found=re.search(r'chrome.css',results)
    assert (css_found != None)

    #b) about page loads a css file that ends in chrome.css
    chrome_driver.get('localhost:8000/about')
    results=chrome_driver.page_source
    css_found=re.search(r'chrome.css',results)
    assert (css_found != None)

    #c) results page loads a css file that ends in chrome.css
    chrome_driver.get('localhost:8000')
    element = chrome_driver.find_element_by_name('query')
    element.send_keys('testing' + Keys.RETURN)
    results=chrome_driver.page_source
    css_found=re.search(r'chrome.css',results)
    assert (css_found != None)

    #d) an empty search returns a page with a css file ending in chrome.css
    chrome_driver.get('localhost:8000')
    element = chrome_driver.find_element_by_name('query')
    element.send_keys('' + Keys.RETURN)
    results=chrome_driver.page_source
    css_found=re.search(r'chrome.css',results)
    assert (css_found != None)
