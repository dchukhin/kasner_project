from selenium import webdriver
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

@pytest.mark.navigate
def test_navigates_to_index_page(w_driver):
    w_driver.get('localhost:8000')

    results=w_driver.page_source
    text_found=re.search(r'Welcome to the Kasner Micro Search Engine', results)
    assert(text_found != None)

@pytest.mark.navigate
def test_navigates_to_about_page(w_driver):
    w_driver.get('localhost:8000/about')

    results=w_driver.page_source
    text_found=re.search(r'About the Kasner Search Engine',results)
    assert(text_found != None)

@pytest.mark.navigate
def test_navigates_to_index_page_then_about_page(w_driver):
    w_driver.get('localhost:8000')

    results=w_driver.page_source
    text_found1=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    w_driver.get('localhost:8000/about')
    results=w_driver.page_source
    text_found2=re.search(r'About the Kasner Search Engine',results)
    
    assert(text_found1 != None and text_found2 != None)

@pytest.mark.navigate
def test_navigates_to_index_page_then_about_page_then_index_page(w_driver):
    w_driver.get('localhost:8000')
    results=w_driver.page_source
    text_found1=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    w_driver.get('localhost:8000/about')
    results=w_driver.page_source
    text_found2=re.search(r'About the Kasner Search Engine',results)

    w_driver.get('localhost:8000')
    results=w_driver.page_source
    text_found3=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    assert(text_found1 != None)
    assert(text_found2 != None)
    assert(text_found3 != None)

@pytest.mark.navigate
def test_navigates_to_index_page_clicks_link_to_about_page_success(w_driver):
    w_driver.get('localhost:8000')
    
    element=w_driver.find_element_by_link_text('About our team').click()
    results=w_driver.page_source
    text_found=re.search(r'About the Kasner Search Engine',results)

    assert(text_found != None)

@pytest.mark.navigate
def test_navigates_to_about_page_clicks_link_to_index_page_success(w_driver):
    w_driver.get('localhost:8000/about')

    element=w_driver.find_element_by_link_text('back to Kasner').click()
    results=w_driver.page_source
    text_found=re.search(r'Welcome to the Kasner Micro Search Engine',results)

    assert(text_found != None)

@pytest.mark.navigate
def test_navigates_to_index_page_then_about_page_then_index_page_success(w_driver):
    w_driver.get('localhost:8000')

    element=w_driver.find_element_by_link_text('About our team').click()
    results=w_driver.page_source
    text_found1=re.search(r'About the Kasner Search Engine',results)

    element=w_driver.find_element_by_link_text('back to Kasner').click()
    results=w_driver.page_source
    text_found2=re.search(r'Welcome to the Kasner Micro Search Engine',results)

    assert(text_found1 != None)
    assert(text_found2 != None)

@pytest.mark.navigate
def test_navigates_to_about_page_then_index_page_then_about_page_success(w_driver):
    w_driver.get('localhost:8000/about')

    element=w_driver.find_element_by_link_text('back to Kasner').click()
    results=w_driver.page_source
    text_found1=re.search(r'Welcome to the Kasner Micro Search Engine',results)

    element=w_driver.find_element_by_link_text('About our team').click()
    results=w_driver.page_source
    text_found2=re.search(r'About the Kasner Search Engine',results)

    assert(text_found1 != None)
    assert(text_found2 != None)

