from selenium import webdriver
from selenium. webdriver.common.keys import Keys
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

@pytest.mark.about
def test_navigates_to_about_page(w_driver):
    w_driver.get('localhost:8000/about')

    results=w_driver.page_source
    text_found=re.search(r'Tweet us!', results)

    assert(text_found != None)

