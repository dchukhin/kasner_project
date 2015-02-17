from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

#for a few tests we use Chrome instead of Firefox
@pytest.fixture(scope="session")
def chrome_driver(request):
    xvfb = Xvfb(width=1280, height=720)
    xvfb.start()
    driver=webdriver.Chrome('/usr/bin/chromedriver')
    request.addfinalizer(driver.quit)
    return driver

def test_new_search_updates_stats(w_driver):
    """Tests if a Kasner search for a new term is reflected in search stats.
    Composed of 3 parts:
    1.) Go to the search stats page and verify that the new search term is 
    not reflected there
    2.) Go to kasner and search for the current time
    3.) Go to the search stats page and verify that the current time is there 
    with a count of 1
    """
    time=str(datetime.datetime.now()).split('.')[0]
    search_term=time
    #1.) Go to the search stats page and verify that the new search term is 
    #not reflected there
    w_driver.get('localhost:8000/search_stats')
    results=w_driver.page_source
    #we are looking for the current time in the page source code
    text_found=re.search(search_term,results)
    #text_found should return as the type None
    assert text_found is None

    #2.) Go to kasner and search for the current time
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys(search_term + Keys.RETURN)

    #3.) Go to the search stats page and verify that the current time is there 
    #as one of the searches with a count of 1
    w_driver.get('localhost:8000/search_stats')

    results=w_driver.page_source
    #we are looking for the current time in the page source code
    text=search_term
    #find the character that begins the reference to the current time
    match = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text)), results)]
    match=match[0]
    #our text is 19 characters long, then there is a space, then the count,
    #which continues until the '>' character, which is displayed as &gt
    count_begins=(match+20)

    character=results[count_begins]
    count=''
    number=count_begins

    #a loop to find the count of the search term 'test'
    while results[number]!= '&':
        count=count+results[number]
        number+=1

    #convert count to an integer
    count=int(count)

    assert (count == 1)

def test_search_updates_stats(w_driver):
    """
    Tests whether a Kasner search engine will update the search stats.

    Composed of 3 parts:
    1.) Go to the search stats page and see how many times the search term
    'test' has been searched for
    2.) Go to kasner and search for 'test'
    3.) Go to the search stats page and verify that the number of times 'test'
    has been searched for has increased by 1
    """
    search_term='test'
    #1.) Go to the search stats page and see how many times the search term
    #'test' has been searched for
    w_driver.get('localhost:8000/search_stats')
    results=w_driver.page_source
    #we are looking for 'SearchTerm: test' in the page source code
    text='SearchTerm: test'
    #find the character that begins the reference to 'SearchTerm: test'
    match = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text)), results)]
    match=match[0]
    #our text is 16 characters long, then there is a space, then the count,
    #which continues until the '>' character, which is displayed as &gt
    count_begins=(match+17)
    
    character=results[count_begins]
    count=''
    number=count_begins

    #a loop to find the count of the search term 'test'
    while results[number]!= '&':
        count=count+results[number]
        number+=1

    #convert count to an integer
    part_1_count=int(count)

    #2.) Go to kasner and search for 'test'
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys(search_term + Keys.RETURN)

    #3.) Go to the search stats page and verify that the number of times 'test'
    #has been searched for has increased by 1
    w_driver.get('localhost:8000/search_stats')

    results=w_driver.page_source
    #we are looking for 'SearchTerm: test' in the page source code
    text='SearchTerm: test'
    #find the character that begins the reference to 'SearchTerm: test'
    match = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text)), results)]
    match=match[0]
    #our text is 16 characters long, then there is a space, then the count,
    #which continues until the '>' character, which is displayed as &gt
    count_begins=(match+17)

    character=results[count_begins]
    count=''
    number=count_begins

    #a loop to find the count of the search term 'test'
    while results[number]!= '&':
        count=count+results[number]
        number+=1

    #convert count to an integer
    part_3_count=int(count)

    assert (part_1_count + 1 == part_3_count)
