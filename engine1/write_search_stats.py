from models import SearchTerm, SearchBrowser
import json

def write_search_terms_stats():
    """
    This function writes a JSON file of the current search terms stats to be 
    loaded by users viewing the search stats.
    """
    terms = list(SearchTerm.objects.filter())
    """
    The terms come as a list and each one is named SearchTerm; we change 
    the terms to make them readable, and then write them to the file.
    """

    #Open a new file for writing.
    file=open('./engine1/templates/stats_terms.json', 'w')
    #Begin the list.
    file.write('[')
    #For each term in the list we write it into the file.
    for term in terms:
        new_term={"name":term.name, "count":term.count}
        file.write(str(json.dumps(new_term)))
        #Add a comma between each term.
        file.write(',')
    #The final term is blank.
    file.write('{}]')
    file.close()

def write_browser_stats():
    """
    This function writes a JSON file of the current browser stats to be 
    loaded by users viewing the search stats.
    """
    browsers = list(SearchBrowser.objects.filter())
    """
    The browsers stats come as a list and each one is named SearchBrowser; we 
    change the terms to make them readable, and then write them to the file.
    """
    #Open a new file for writing.
    file=open('./engine1/templates/stats_browsers.json', 'w')
    #Begin the list.
    file.write('[')
    #For each term in the list we write it into the file.
    for browser in browsers:
        new_browser_term={"name":browser.name, "count":browser.count}
        file.write(str(json.dumps(new_browser_term)))
        #Add a comma between each term.
        file.write(',')
        #The final term is blank.
    file.write('{}]')
    file.close()
