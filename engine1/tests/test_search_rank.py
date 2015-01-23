from selenium import webdriver
from selenium. webdriver.common.keys import Keys
from xvfbwrapper import Xvfb
import re
import pytest

@pytest.fixture(scope="session")
def w_driver(request):
    xvfb = Xvfb(width=1280,height=720)
    xvfb.start()
    driver=webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver

def test_pages_with_same_name_ranked_by_number(w_driver):
    """
    Tests whether websites with same name are ranked descending in results.

    1.) Add two websites with same name, but different number into db
    2.) Do a Kasner search and verify that the websites are sorted in 
    descending order in the search results.
    """
    w_driver.get('localhost:8000/add_form')
    #1.) Add two websites with same name, but different number into db
    #First site, with number=5
    name_element=w_driver.find_element_by_name('name')
    name_element.send_keys('test site')
    url_element=w_driver.find_element_by_name('url')
    url_element.send_keys('www.testsitewithnumber5.com')
    number_element=w_driver.find_element_by_name('number')
    number_element.send_keys(5)
    name_element.send_keys(Keys.RETURN)

    #Second site, with number=6
    name_element=w_driver.find_element_by_name('name')
    name_element.send_keys('test site')
    url_element=w_driver.find_element_by_name('url')
    url_element.send_keys('www.testsitewithnumber6.com')
    number_element=w_driver.find_element_by_name('number')
    number_element.send_keys(6)
    name_element.send_keys(Keys.RETURN)

    #2.) Do a Kasner search and verify that the websites are sorted in 
    #    descending order in the search results.
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('test site' + Keys.RETURN)

    results=w_driver.page_source
    #results should list testsitewithnumber6.com before testsitewithnumber5.com
    text6='www.testsitewithnumber6.com' 
    #find the character that begins the reference to testsitewithnumber6.com
    matches6 = [matches.start() 
    for matches in re.finditer(r'{}'.format(re.escape(text6)), results)]
    #there are 2 references for testsitewithnumber6.com; we get the first.
    matches6=matches6[0]

    #find the character that begins the reference to testsitewithnumber5.com
    text5='www.testsitewithnumber5.com'               
    matches5 = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text5)), results)]
    #there are 2 references for testsitewithnumber5.com. we get the first.
    matches5=matches5[0]

    #matches6 should occur first, so its reference character should be smaller
    assert (matches6<matches5)

def test_name_matches_ranked_higher_than_wikipedia(w_driver):
    """
    Tests if website with name match are ranked higher than wikipedia matches.

    1.) Add a test websites into db
    2.) Do a Kasner search and verify that the website is ranked higher than 
    the wikipedia result for the query.
    """
    w_driver.get('localhost:8000/add_form')
    #1.) Add a test website into db
    name_element=w_driver.find_element_by_name('name')
    name_element.send_keys('test site')
    url_element=w_driver.find_element_by_name('url')
    url_element.send_keys('www.testsitewithnumber5.com')
    number_element=w_driver.find_element_by_name('number')
    number_element.send_keys(5)
    name_element.send_keys(Keys.RETURN)

    #2.) Do a Kasner search and verify that the website is ranked higher than 
    #the wikipedia result for the query.
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('test site' + Keys.RETURN)

    results=w_driver.page_source
    #results should list testsitewithnumber5.com before wikipedia result
    text5='www.testsitewithnumber5.com' 
    #find the character that begins the reference to testsitewithnumber6.com
    matches5 = [matches.start() 
    for matches in re.finditer(r'{}'.format(re.escape(text5)), results)]
    #there are 2 references for testsitewithnumber6.com; we get the first.
    matches5=matches5[0]

    text_wikip='wikipedia.org/wiki/test'
    #find the character that begins the reference to wikipedia site
    matches_wikip = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text_wikip)),results)]
    #there are 2 references for the url; we get the first.
    matches_wikip=matches_wikip[0]

    #matches5 should occur first, so its reference character should be smaller
    assert (matches5<matches_wikip)

def test_name_matches_ranked_higher_than_keyword_matches(w_driver):
    """
    Tests if website with name match are ranked higher than keyword matches.

    1.) Add a test website into db with name=test site
    2.) Add 2 websites into db with keyword=test site
    3.) Do a Kasner search and verify that the website with name=test is
    ranked higher than the websites with keyword=tests.
    """
    w_driver.get('localhost:8000/add_form')
    #1.) Add a test website into db with name=test
    name_element=w_driver.find_element_by_name('name')
    name_element.send_keys('test site')
    url_element=w_driver.find_element_by_name('url')
    url_element.send_keys('www.testsitewithnumber5.com')
    number_element=w_driver.find_element_by_name('number')
    number_element.send_keys(5)
    number_element.send_keys(Keys.RETURN)

    #2.) Add 2 websites into db with keyword=test site
    name_element1=w_driver.find_element_by_name('name')
    name_element1.send_keys('first one')
    url_element1=w_driver.find_element_by_name('url')
    url_element1.send_keys('www.firstsite5.com')
    number_element1=w_driver.find_element_by_name('number')
    number_element1.send_keys(5)
    words_element1=w_driver.find_element_by_name('words')
    words_element1.send_keys('test site')
    words_element1.send_keys(Keys.RETURN)

    name_element2=w_driver.find_element_by_name('name')
    name_element2.send_keys('first one')
    url_element2=w_driver.find_element_by_name('url')
    url_element2.send_keys('www.secondsite5.com')
    number_element2=w_driver.find_element_by_name('number')
    number_element2.send_keys(5)
    words_element2=w_driver.find_element_by_name('words')
    words_element2.send_keys('test site')
    words_element2.send_keys(Keys.RETURN)

    #3.) Do a Kasner search and verify that the website with name=test is
    #ranked higher than the websites with keyword=tests.
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys('test site' + Keys.RETURN)

    results=w_driver.page_source
    #results should list testsitewithnumber5.com before keyword match results
    text5='www.testsitewithnumber5.com'
    #find the character that begins the reference to testsitewithnumber5.com
    matches5 = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text5)), results)]
    #there are 2 references for testsitewithnumber6.com; we get the first.
    matches5=matches5[0]

    text_kw_1='www.firstsite5.com'
    #find the character that begins the reference to www.firstsite5.com
    matches_kw_1 = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text_kw_1)),results)]
    #there are 2 references for the url; we get the first.
    matches_kw_1=matches_kw_1[0]

    text_kw_2='www.secondsite5.com'
    #find the character that begins the reference to www.firstsite5.com
    matches_kw_2 = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text_kw_2)),results)]
    #there are 2 references for the url; we get the first.
    matches_kw_2=matches_kw_2[0]

    #www.testsitewithnumber5.com should occur first
    assert (matches5<matches_kw_1)
    assert (matches5<matches_kw_2)

@pytest.mark.new
def test_wikipedia_matches_ranked_higher_than_keyword_matches(w_driver):
    """
    Tests if website with name match is ranked higher than keyword matches.

    1.) Add 2 websites into db with keyword=test site
    2.) Do a Kasner search and verify that the websites with keyword=tests is
    ranked higher than the wikipedia site.
    """
    keyword='test site'
    w_driver.get('localhost:8000/add_form')
    
    #1.) Add 2 websites into db with keyword=test site
    name_element1=w_driver.find_element_by_name('name')
    name_element1.send_keys('first one')
    url_element1=w_driver.find_element_by_name('url')
    url_element1.send_keys('www.firstsite5.com')
    number_element1=w_driver.find_element_by_name('number')
    number_element1.send_keys(5)
    words_element1=w_driver.find_element_by_name('words')
    words_element1.send_keys(keyword)
    words_element1.send_keys(Keys.RETURN)

    name_element2=w_driver.find_element_by_name('name')
    name_element2.send_keys('first one')
    url_element2=w_driver.find_element_by_name('url')
    url_element2.send_keys('www.secondsite5.com')
    number_element2=w_driver.find_element_by_name('number')
    number_element2.send_keys(5)
    words_element2=w_driver.find_element_by_name('words')
    words_element2.send_keys(keyword)
    words_element2.send_keys(Keys.RETURN)

    #2.) Do a Kasner search and verify that the websites with keyword=tests is
    #ranked higher than the wikipedia site.
    w_driver.get('localhost:8000')
    element = w_driver.find_element_by_name('query')
    element.send_keys(keyword + Keys.RETURN)

    results=w_driver.page_source
    #results should list wikipedia site before keyword match results
    text_wikip='wikipedia.org/wiki/'+keyword
    #find the character that begins the reference to wikipedia site 
    matches_wikip = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text_wikip)), results)]
    #there are 2 references for wikipedia site; we get the first.
    matches_wikip=matches_wikip[0]

    text_kw_1='www.firstsite5.com'
    #find the character that begins the reference to www.firstsite5.com
    matches_kw_1 = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text_kw_1)),results)]
    #there are 2 references for the url; we get the first.
    matches_kw_1=matches_kw_1[0]

    text_kw_2='www.secondsite5.com'
    #find the character that begins the reference to www.firstsite5.com
    matches_kw_2 = [matches.start()
    for matches in re.finditer(r'{}'.format(re.escape(text_kw_2)),results)]
    #there are 2 references for the url; we get the first.
    matches_kw_2=matches_kw_2[0]
    
    assert (matches_wikip<matches_kw_1)
    assert (matches_wikip<matches_kw_2)
