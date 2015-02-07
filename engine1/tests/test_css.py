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

def test_background_image_loads(w_driver):
    """
    Test verifies that the background image loads on all user pages.

    User pages include:
    1.) index page
    2.) results page
    3.) about page
    """
    #1.) Index Page
    w_driver.get('localhost:8000')
    #the url to our background image
    expected_image='url("http://localhost:8000/static/engine1/banner.jpg")'
    element = w_driver.find_element_by_id('banner')
    #we get the value of the background image, which is a url to its source
    actual_image=element.value_of_css_property('background-image')
    assert(expected_image==actual_image)
   
    #2.) Results Page
    w_driver.get('localhost:8000')
    #we search for something to pull up the results page
    element = w_driver.find_element_by_name('query')
    element.send_keys('o' + Keys.RETURN)
   
    #the url to our background image
    expected_image='url("http://localhost:8000/static/engine1/banner.jpg")'
    element = w_driver.find_element_by_id('banner')
    #we get the value of the background image, which is a url to its source
    actual_image=element.value_of_css_property('background-image')
    assert(expected_image==actual_image)

    #3.) About Page
    w_driver.get('localhost:8000/about')
    #the url to our background image
    expected_image='url("http://localhost:8000/static/engine1/banner.jpg")'
    element = w_driver.find_element_by_id('banner')
    #we get the value of the background image, which is a url to its source
    actual_image=element.value_of_css_property('background-image')
    assert(expected_image==actual_image)

def test_backgound_color(w_driver):
    """
    Tests background colors of pages.

    1.) index page: black
    2.) results page: white
    3.) about page: white
    """
    #1.) Index Page
    w_driver.get('localhost:8000')
    element=w_driver.find_element_by_class_name('container')
    #the background color is #000000, which maps to rgba(0, 0, 0, 1)
    expected_color = 'rgba(0, 0, 0, 1)'
    actual_color = element.value_of_css_property('background-color')
    assert(expected_color == actual_color)
    element=w_driver.find_element_by_class_name('container1')
    #the background color is grey, which maps to rgba(128, 128, 128, 1)
    expected_color = 'rgba(128, 128, 128, 1)'
    actual_color = element.value_of_css_property('background-color')
    assert(expected_color == actual_color)


    #2.) Results Page
    w_driver.get('localhost:8000')
    #we search for something to pull up the results page
    element = w_driver.find_element_by_name('query')
    element.send_keys('o' + Keys.RETURN)

    element=w_driver.find_element_by_class_name('container')
    #the background color is white, which maps to rgba(255, 255, 255, 1)
    expected_color = 'rgba(255, 255, 255, 1)'
    actual_color = element.value_of_css_property('background-color')
    assert(expected_color == actual_color)

    #3.) About Page
    w_driver.get('localhost:8000/about')
    element=w_driver.find_element_by_class_name('container')
    #the background color is white, which maps to rgba(255, 255, 255, 1)
    expected_color = 'rgba(255, 255, 255, 1)'
    actual_color = element.value_of_css_property('background-color')
    assert(expected_color == actual_color)
    element=w_driver.find_element_by_class_name('container1')
    #the background color is white, which maps to rgba(255, 255, 255, 1)
    expected_color = 'rgba(255, 255, 255, 1)'
    actual_color = element.value_of_css_property('background-color')
    assert(expected_color == actual_color)

def test_div_rounded_corners(w_driver, chrome_driver):
    """Tests if div elements have rounded corners.
    Test verifies rounded corners for:
    1.) Firefox
        a) 'container-thirds' div elements on the index page
        b) banner with searchbox on about page
        c) 'container-halves' div elements on about page
        d) banner with searchbox on results page
    2.) Chrome
        a) 'container-thirds' div elements on the index page
        b) banner with searchbox and reflection on about page
        c) 'container-halves' div elements on about page
        d) banner with searchbox and reflection on results page
    """
    #1.) Firefox
    w_driver.get('localhost:8000')
    #a) 'div-thirds' elements on the index page
    element=w_driver.find_element_by_class_name('container-thirds')
    expected_value='5px'
    #actual border-radius values are top-left, top-right, and so on
    actual_val_t_l=element.value_of_css_property('border-top-left-radius')
    actual_val_t_r=element.value_of_css_property('border-top-right-radius')
    actual_val_b_r=element.value_of_css_property('border-bottom-right-radius')
    actual_val_b_l=element.value_of_css_property('border-bottom-left-radius')
    
    actual_vals=[actual_val_t_l,actual_val_t_r,actual_val_b_r,actual_val_b_l]
    for val in actual_vals:
        assert (expected_value == val)

    #b) banner with searchbox on about page
    w_driver.get('localhost:8000/about')
    element=w_driver.find_element_by_id('banner-with-searchbox-firefox')
    expected_value='5px'
    #actual border-radius values are top-left, top-right, and so on
    actual_val_t_l=element.value_of_css_property('border-top-left-radius')
    actual_val_t_r=element.value_of_css_property('border-top-right-radius')
    actual_val_b_r=element.value_of_css_property('border-bottom-right-radius')
    actual_val_b_l=element.value_of_css_property('border-bottom-left-radius')

    actual_vals=[actual_val_t_l,actual_val_t_r,actual_val_b_r,actual_val_b_l]
    for val in actual_vals:
        assert (expected_value == val)

    #c) 'div-halves' elements on about page
    element=w_driver.find_element_by_class_name('container-halves')
    expected_value='5px'
    #actual border-radius values are top-left, top-right, and so on
    actual_val_t_l=element.value_of_css_property('border-top-left-radius')
    actual_val_t_r=element.value_of_css_property('border-top-right-radius')
    actual_val_b_r=element.value_of_css_property('border-bottom-right-radius')
    actual_val_b_l=element.value_of_css_property('border-bottom-left-radius')

    actual_vals=[actual_val_t_l,actual_val_t_r,actual_val_b_r,actual_val_b_l]
    for val in actual_vals:
        assert (expected_value == val)

    #d) banner with searchbox on results page
    w_driver.get('localhost:8000')
    #we search for something to pull up the results page
    element = w_driver.find_element_by_name('query')
    element.send_keys('o' + Keys.RETURN)

    element=w_driver.find_element_by_id('banner-with-searchbox-firefox')
    expected_value='5px'
    #actual border-radius values are top-left, top-right, and so on
    actual_val_t_l=element.value_of_css_property('border-top-left-radius')
    actual_val_t_r=element.value_of_css_property('border-top-right-radius')
    actual_val_b_r=element.value_of_css_property('border-bottom-right-radius')
    actual_val_b_l=element.value_of_css_property('border-bottom-left-radius')

    actual_vals=[actual_val_t_l,actual_val_t_r,actual_val_b_r,actual_val_b_l]
    for val in actual_vals:
        assert (expected_value == val)

    #2.) Chrome
    #a) 'container-thirds' div elements on the index page
    chrome_driver.get('localhost:8000')
    element=chrome_driver.find_element_by_class_name('container-thirds')
    expected_value='5px'
    #actual border-radius values are top-left, top-right, and so on
    actual_val_t_l=element.value_of_css_property('border-top-left-radius')
    actual_val_t_r=element.value_of_css_property('border-top-right-radius')
    actual_val_b_r=element.value_of_css_property('border-bottom-right-radius')
    actual_val_b_l=element.value_of_css_property('border-bottom-left-radius')

    actual_vals=[actual_val_t_l,actual_val_t_r,actual_val_b_r,actual_val_b_l]
    for val in actual_vals:
        assert (expected_value == val)

    #b) banner with searchbox and reflection on about page
    chrome_driver.get('localhost:8000/about')
    element=chrome_driver.find_element_by_id('banner-with-searchbox-chrome')
    expected_value='5px'
    #actual border-radius values are top-left, top-right, and so on
    actual_val_t_l=element.value_of_css_property('border-top-left-radius')
    actual_val_t_r=element.value_of_css_property('border-top-right-radius')
    actual_val_b_r=element.value_of_css_property('border-bottom-right-radius')
    actual_val_b_l=element.value_of_css_property('border-bottom-left-radius')

    actual_vals=[actual_val_t_l,actual_val_t_r,actual_val_b_r,actual_val_b_l]
    for val in actual_vals:
        assert (expected_value == val)
    #c) 'container-halves' div elements on about page
    chrome_driver.get('localhost:8000/about')
    element=chrome_driver.find_element_by_class_name('container-halves')
    expected_value='5px'
    #actual border-radius values are top-left, top-right, and so on
    actual_val_t_l=element.value_of_css_property('border-top-left-radius')
    actual_val_t_r=element.value_of_css_property('border-top-right-radius')
    actual_val_b_r=element.value_of_css_property('border-bottom-right-radius')
    actual_val_b_l=element.value_of_css_property('border-bottom-left-radius')

    actual_vals=[actual_val_t_l,actual_val_t_r,actual_val_b_r,actual_val_b_l]
    for val in actual_vals:
        assert (expected_value == val)

    #d) banner with searchbox and reflection on results page
    chrome_driver.get('localhost:8000')
    #we search for something to pull up the results page
    element = chrome_driver.find_element_by_name('query')
    element.send_keys('o' + Keys.RETURN)

    element=chrome_driver.find_element_by_id('banner-with-searchbox-chrome')
    expected_value='5px'
    #actual border-radius values are top-left, top-right, and so on
    actual_val_t_l=element.value_of_css_property('border-top-left-radius')
    actual_val_t_r=element.value_of_css_property('border-top-right-radius')
    actual_val_b_r=element.value_of_css_property('border-bottom-right-radius')
    actual_val_b_l=element.value_of_css_property('border-bottom-left-radius')

    actual_vals=[actual_val_t_l,actual_val_t_r,actual_val_b_r,actual_val_b_l]
    for val in actual_vals:
        assert (expected_value == val)

def test_div_container(w_driver, chrome_driver):
    """Tests whether the div 'container-wide' element is correct size.
    Test looks at:
    1.) Firefox:
    a) Index Page
    b) About Page
    2.) Chrome:
        a) Index Page
        b) About Page

    """
    #1.) Firefox
    #a) Index Page
    w_driver.get('localhost:8000')
    #get actual screen width
    screen_size=w_driver.get_window_size()
    screen_width=screen_size['width']

    #actual div width
    element=w_driver.find_element_by_class_name('container-wide')
    actual_value=element.value_of_css_property('width')
    #actual_value is something like 800px; we get just the integer
    actual_value=int(re.match(r'\d+', actual_value).group())

    #we expect the div to be 100% of screen width, but allow 5% error
    assert (screen_width*0.95 < actual_value)
    
    #b) About Page
    w_driver.get('localhost:8000/about')
    #get actual screen width
    screen_size=w_driver.get_window_size()
    screen_width=screen_size['width']

    #actual div width
    element=w_driver.find_element_by_class_name('container-wide')
    actual_value=element.value_of_css_property('width')
    #actual_value is something like 800px; we get just the integer
    actual_value=int(re.match(r'\d+', actual_value).group())

    #we expect the div to be 100% of screen width, but allow 5% error
    assert (screen_width*0.95 < actual_value)

    #2.) Chrome
    #a) Index Page
    chrome_driver.get('localhost:8000')
    #get actual screen width
    screen_size=w_driver.get_window_size()
    screen_width=screen_size['width']

    #actual div width
    element=chrome_driver.find_element_by_class_name('container-wide')
    actual_value=element.value_of_css_property('width')
    #actual_value is something like 800px; we get just the integer
    actual_value=int(re.match(r'\d+', actual_value).group())

    #we expect the div to be 100% of screen width, but allow 5% error
    assert (screen_width*0.95 < actual_value)

    #b) About Page
    chrome_driver.get('localhost:8000/about')
    #get actual screen width
    screen_size=w_driver.get_window_size()
    screen_width=screen_size['width']

    #actual div width
    element=chrome_driver.find_element_by_class_name('container-wide')
    actual_value=element.value_of_css_property('width')
    #actual_value is something like 800px; we get just the integer
    actual_value=int(re.match(r'\d+', actual_value).group())

    #we expect the div to be 100% of screen width, but allow 5% error
    assert (screen_width*0.95 < actual_value)


