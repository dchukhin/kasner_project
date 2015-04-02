from models import SearchTerm, SearchBrowser
import json

def write(for_what, folder):
    """
    This function calls the other functions in this file. It seemed easier to 
    call a single function (this one) from a different file, rather than 
    calling the other functions in this file from other files. This write 
    function: 
        1.) determines which function needs to be called, and calls it, or 
        2.) raises a ValueError that the arguments for_what and folder were
        not valid.
    """
    if (for_what == 'search_terms' and folder == 'templates'):
        write_search_terms_stats()
    elif (for_what == 'browsers' and folder == 'templates'):
        write_browser_stats()
    else:
        raise ValueError ('''At this point this function can only write '''
                '''json files for search_terms and browsers into the '''
                '''templates folder. You tried: ''', for_what, '''into '''
                '''the ''', folder, '''folder.''')

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
    print 'search terms success'

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
