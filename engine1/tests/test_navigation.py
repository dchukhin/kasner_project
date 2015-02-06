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


def test_navigates_to_index_page(w_driver):
    w_driver.get('localhost:8000')

    results=w_driver.page_source
    text_found=re.search(r'Welcome to the Kasner Micro Search Engine', results)
    assert(text_found != None)

def test_navigates_to_about_page(w_driver):
    w_driver.get('localhost:8000/about')

    results=w_driver.page_source
    text_found=re.search(r'About the Kasner Search Engine',results)
    assert(text_found != None)

def test_navigates_to_index_page_about_page(w_driver):
    """Test navigating to index page, then change the url to the about page
   
    1.) Go to index page url
    2.) Go to about page url
    Note: this test does not test links between these two pages.
    """
    #Index Page
    w_driver.get('localhost:8000')
    results=w_driver.page_source
    text_found1=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    #About Page
    w_driver.get('localhost:8000/about')
    results=w_driver.page_source
    text_found2=re.search(r'About the Kasner Search Engine',results)
   
    assert(text_found1 != None and text_found2 != None)

def test_navigates_to_index_page_about_page_index_page(w_driver):
    """
    Test navigating to index page, then the about page, then the index page
   
    1.) go to index page url
    2.) go to about page url
    3.) go to index page url
    Note: this test does not test links between these pages.
    """
    #Index Page
    w_driver.get('localhost:8000')
    results=w_driver.page_source
    text_found1=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    #About Page
    w_driver.get('localhost:8000/about')
    results=w_driver.page_source
    text_found2=re.search(r'About the Kasner Search Engine',results)

    #Index Page
    w_driver.get('localhost:8000')
    results=w_driver.page_source
    text_found3=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    assert(text_found1 != None)
    assert(text_found2 != None)
    assert(text_found3 != None)

def test_navigates_to_index_page_link_about_page(w_driver):
    """Tests whether the link on index page to go to about page works."""
    w_driver.get('localhost:8000')
   
    element=w_driver.find_element_by_link_text('About our team').click()
    results=w_driver.page_source
    text_found=re.search(r'About the Kasner Search Engine',results)

    assert(text_found != None)

def test_navigates_to_about_page_link_index_page(w_driver):
    """Tests whether the link on about page to go to index page works."""
    w_driver.get('localhost:8000/about')

    element=w_driver.find_element_by_link_text('back to Kasner').click()
    results=w_driver.page_source
    text_found=re.search(r'Welcome to the Kasner Micro Search Engine',results)

    assert(text_found != None)

def test_navigates_to_index_page_then_about_page_then_index_page_success(w_driver):
    """Tests whether the links between index page and about page work.
   
    1.) Navigate to index page, click link for about page, get about page info
    2.) Click link for index page, get index page info
    3.) Verify info we found is not None
    """
    #1.) Navigate to index page, click link for about page
    w_driver.get('localhost:8000')

    element=w_driver.find_element_by_link_text('About our team').click()
    #find about page info
    results=w_driver.page_source
    text_found1=re.search(r'About the Kasner Search Engine',results)

    #2.) Click link for index page
    element=w_driver.find_element_by_link_text('back to Kasner').click()
    #find index page info
    results=w_driver.page_source
    text_found2=re.search(r'Welcome to the Kasner Micro Search Engine',results)

    #3.) Verify info we found is not None
    assert(text_found1 != None)
    assert(text_found2 != None)

def test_navigates_to_about_page_then_index_page_then_about_page_success(w_driver):
    """Tests whether the links between index page and about page work.
   
    1.) Navigate to index page, click link for about page, get about page info
    2.) Click link for index page, get index page info
    3.) Verify info we found is not None
    """
    #1.) Navigate to about page, click link for index page
    w_driver.get('localhost:8000/about')

    element=w_driver.find_element_by_link_text('back to Kasner').click()
    #find index page info
    results=w_driver.page_source
    text_found1=re.search(r'Welcome to the Kasner Micro Search Engine',results)

    #2.) Click link for index page
    element=w_driver.find_element_by_link_text('About our team').click()
    #find about page info
    results=w_driver.page_source
    text_found2=re.search(r'About the Kasner Search Engine',results)

    #3.) Verify info we found is not None
    assert(text_found1 != None)
    assert(text_found2 != None)

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
