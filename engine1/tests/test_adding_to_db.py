from selenium import webdriver
from selenium. webdriver.common.keys import Keys
import re
import pytest

@pytest.fixture(scope="session")
def w_driver(request):
    driver=webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver

browser=webdriver.Firefox()

@pytest.mark.easy
def test_navigates_to_kasner(w_driver):
    w_driver.get('localhost:8000')
    
    results=w_driver.page_source
    text_found=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    assert(text_found != None)

import datetime
time=str(datetime.datetime.now()).split('.')[0]

def test_add_webpage_to_db(w_driver):
    """
    Part 1.) add a unique (not previously existing) website to db
    Part 2.) verify the website we added comes up as a result in Kasner
    """
    w_driver.get('localhost:8000/add_form')
    #part 1.) add a unique (not previously existing) website to db
    
    #name element is given a website name with the current time
    name_element=w_driver.find_element_by_name('name')
    name_element.send_keys(time)
    
    test_url = 'www.'+time+'.com'
    url_element=w_driver.find_element_by_name('url')
    url_element.send_keys(test_url)
    
    number_element=w_driver.find_element_by_name('number')
    number_element.send_keys(5)

    name_element.send_keys(Keys.RETURN)

    #part 2.) verify the website we added comes up as a result in Kasner
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys(time + Keys.RETURN)

    results=w_driver.page_source
    text_found=re.search(time, results)

    assert text_found != None

@pytest.mark.slow
def test_update_website_already_in_db(w_driver):
    """
    Part 1.) add a website to db
    Part 2.) add the same website with different website name
    Part 3.) verify that the website has the new name when seared in Kasner
    """
    # Part 1.)
    w_driver.get('localhost:8000/add_form')

    #name element is given a website name with the current time
    name_element=w_driver.find_element_by_name('name')
    name_element.send_keys(time)

    test_url = 'www.'+time+'.com'
    url_element=w_driver.find_element_by_name('url')
    url_element.send_keys(test_url)

    number_element=w_driver.find_element_by_name('number')
    number_element.send_keys(5)

    name_element.send_keys(Keys.RETURN)

    # Part 2.) we keep the url the same as before, but the name is new_time
    w_driver.get('localhost:8000/add_form')

    new_time=str(datetime.datetime.now()).split('.')[0]
    name_element=w_driver.find_element_by_name('name')
    name_element.send_keys(new_time)

    test_url = 'www.'+time+'.com'
    url_element=w_driver.find_element_by_name('url')
    url_element.send_keys(test_url)

    number_element=w_driver.find_element_by_name('number')
    number_element.send_keys(5)

    name_element.send_keys(Keys.RETURN)

    #Part 3.) When we search in Kasner, the website should be found with
    #the new_time as its name and time as a part of its url
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys(new_time + Keys.RETURN)

    results=w_driver.page_source
    search_output=new_time+' at www.'+time+'.com'
    new_time_found=re.search(search_output, results)

    assert new_time_found != None

#    browser.quit()

