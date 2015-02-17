from selenium import webdriver
from selenium. webdriver.common.keys import Keys
from xvfbwrapper import Xvfb
import re
import pytest
import datetime

@pytest.fixture(scope="session")
def w_driver(request):
    xvfb = Xvfb(width=1280, height=720)
    xvfb.start()
    driver=webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver

@pytest.mark.easy
def test_navigates_to_kasner(w_driver):
    w_driver.get('localhost:8000')
    
    results=w_driver.page_source
    text_found=re.search(r'Welcome to the Kasner Micro Search Engine', results)

    assert(text_found != None)

time=str(datetime.datetime.now()).split('.')[0]

def test_add_webpage_to_db(w_driver):
    """
    Test to add a webpage to the db, then to verify that it was added.
    
    Part 1.) add a unique (not previously existing) website to db
    Part 2.) verify the website we added comes up as a result in Kasner
    """
    w_driver.get('localhost:8000/add_form')
    #Part 1.) add a unique (not previously existing) website to db
    
    #name element is given a website name with the current time
    name_element=w_driver.find_element_by_name('name')
    name_element.send_keys(time)
    
    test_url = 'www.'+time+'.com'
    url_element=w_driver.find_element_by_name('url')
    url_element.send_keys(test_url)
    
    number_element=w_driver.find_element_by_name('number')
    number_element.send_keys(5)

    name_element.send_keys(Keys.RETURN)

    #Part 2.) verify the website we added comes up as a result in Kasner
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys(time + Keys.RETURN)

    results=w_driver.page_source
    text_found=re.search(time, results)

    assert text_found != None

def test_update_website_already_in_db(w_driver):
    """
    Test to update a website that already exists in our database.
    
    Part 1.) add a website to database
    Part 2.) add the same website with different website name
    Part 3.) verify that the website has the new name when searched in Kasner
    """
    #Part 1.) add a website to databse
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

    #Part 2.) we keep the url the same as before, but the name is new_time
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

    #the time, which reads as something like 2014-01-01 12:00:00 will be
    #shown in the page source as 2014-01-01%2012:00:00.
    #we create the ref_time variable to match that
    ref_time=time[0:10]+'%20'+time[11:19]

    #the search output should say the new_time at www.time.com. There is an 
    #href, so the page source has that in it, as well as a few spaces
    ref_to_site='\n                <a href="'+'http://www.'+ref_time+'.com'
    search_output=new_time+' at '+ref_to_site
    new_time_found=re.search(search_output, results)

    assert new_time_found != None

