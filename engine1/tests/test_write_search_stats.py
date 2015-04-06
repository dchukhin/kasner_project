import json
from django.conf import settings
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'kasner.settings'
import django
django.setup()

from .. import write_search_stats
import pytest

def test_write_json_file_for_browsers_templates():
    """
    This test attempts to call write_search_stats to write a JSON file for the
    stats in the DB, with the first argument as 'browsers' and the second 
    argument as 'templates'.
    write_search_terms accepts 2 arguments:
        1. The first must be 'browsers' or 'search_terms'
        2. The second must be 'templates'
    There should be no error message raised.
    This test:
        1.) Verifies no errors are raised when calling write_search_stats with 
        'browsers' and 'templates' as the arguments.
        2.) Verifies stats_browsers.json file created by write_search_terms 
        matches the output from DB.
    """
    """
    1.) Verifies no errors are raised when calling write_search_stats with 
       'browsers' and 'templates' as the arguments.
    """
    term = 'browsers'
    folder = 'templates'
    try:
        write_search_stats.write(term, folder)
    except ValueError:
        pytest.fail("Unexpected Error")

    """
    2.) Verifies the stats_browsers.json file created by write_search_terms 
       matches the output from DB.
    """
    #a) get values from db
    from ..models import SearchBrowser
    browsers = list(SearchBrowser.objects.filter())
    #change the browsers to just the names and the counts
    browsers_list = []
    for browser in browsers:
        browser = {"name":browser.name, "count":browser.count}
        browsers_list.append(browser)

    #b) get values from stats_browsers
    base_directory = settings.BASE_DIR
    template_directory = base_directory + '/engine1/templates/'
    browser_file = 'stats_browsers.json'
    file=open(template_directory + browser_file, 'r')
    contents_of_file = file.read()
    #the contents of the file will be read as a string; convert to JSON
    json_file = json.loads(contents_of_file)

    """
    c) check that a) and b) are the same:
        i) check that length of list in part a ==  length of list in part b
        ii) check for each element from part a is in list in part b
    """
    #i) check that length of list in part a ==  length of list in part b
    assert (len(browsers_list) == len(json_file))
    #ii) check for each element from part a is in list in part b
    for element in browsers_list:
        assert element in json_file

def test_write_json_file_for_incorrect_db_term():
    """
    This test attempts to call write_search_stats to write a JSON file for the
    stats in the DB, but the first argument is random characters, instead of 
    'search_terms' or 'browsers'.
    write_search_terms accepts 2 arguments:
        1. The first must be 'browsers' or 'search_terms'
        2. The second must be 'templates'
    Thus, this call to write_search_terms should fail with a ValueError being 
    raised.
    """
    term = 'lwgswfoifdsj'
    folder = 'templates'
    with pytest.raises(ValueError) as error_message:
        write_search_stats.write(term, folder)
    exp_err_l1 = "ValueError: ('At this point this function can only write "
    exp_err_l2 = "json files for search_terms and browsers into the templates "
    exp_err_l3 = "folder. You tried: ', '" + term + "', 'into the ', "
    exp_err_l4 = "'" + folder +"', 'folder.')"
    expected_error = exp_err_l1 + exp_err_l2 + exp_err_l3 + exp_err_l4
    assert error_message.exconly() == expected_error

def test_write_json_file_for_incorrect_folder():
    """
    This test attempts to call write_search_stats to write a JSON file for the
    stats in the DB, but the second argument is random characters, instead of 
    'search_terms' or 'browsers'.
    write_search_terms accepts 2 arguments:
        1. The first must be 'browsers' or 'search_terms'
        2. The second must be 'templates'
    Thus, this call to write_search_terms should fail with a ValueError being 
    raised.
    """
    term = 'browsers'
    folder = 'sdkljfkd'
    with pytest.raises(ValueError) as error_message:
        write_search_stats.write(term, folder)
    exp_err_l1 = "ValueError: ('At this point this function can only write "
    exp_err_l2 = "json files for search_terms and browsers into the templates "
    exp_err_l3 = "folder. You tried: ', '" + term + "', 'into the ', "
    exp_err_l4 = "'" + folder +"', 'folder.')"
    expected_error = exp_err_l1 + exp_err_l2 + exp_err_l3 + exp_err_l4
    assert error_message.exconly() == expected_error

def test_write_json_file_for_incorrect_db_term_incorrect_folder():
    """
    This test attempts to call write_search_stats to write a JSON file for the
    stats in the DB, but the first argument is random characters, instead of 
    'search_terms' or 'browsers' and the second argument is random characters
    instead of 'templates'.
    write_search_terms accepts 2 arguments:
        1. The first must be 'browsers' or 'search_terms'
        2. The second must be 'templates'
    Thus, this call to write_search_terms should fail with a ValueError being 
    raised.
    """
    term = 'kjdsfkjd'
    folder = '23jrkrsdfkj'
    with pytest.raises(ValueError) as error_message:
        write_search_stats.write(term, folder)
    exp_err_l1 = "ValueError: ('At this point this function can only write "
    exp_err_l2 = "json files for search_terms and browsers into the templates "
    exp_err_l3 = "folder. You tried: ', '" + term + "', 'into the ', "
    exp_err_l4 = "'" + folder +"', 'folder.')"
    expected_error = exp_err_l1 + exp_err_l2 + exp_err_l3 + exp_err_l4
    assert error_message.exconly() == expected_error

