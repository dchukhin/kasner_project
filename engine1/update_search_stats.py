from models import SearchTerm, SearchBrowser

def update_search_stats(query, browser):
    """
    Here we update the stats in the database for the SearchTerm and the browser.

    We start by searching for our SearchTerm and browser in the database.
    In Part 1 we see if the SearchTerm already exists, and if so, we add 1
    to its counter. If not, we create a new SearchTerm in the database and 
    set its count to 1.
    In Part 2 we see if the SearchBrowser already exists, and if so, we add 1
    to its counter. If not, we create a new SearchBrowser in the database and 
    set its count to 1.
    """
    SearchTerm_exists=SearchTerm.objects.filter(name=query).exists()
    SearchBrowser_exists=SearchBrowser.objects.filter(name=browser).exists()
    #1.) The SearchTerm
    #if the search term already exists in the database
    if SearchTerm_exists == True:
        newSearchTerm=SearchTerm.objects.get(name=query)
        #find the count
        count=newSearchTerm.count
        #increase the count by 1
        count+=1
        newSearchTerm.count=count
        newSearchTerm.save()
    #if the search term does not exist yet
    elif (SearchTerm_exists == False):
        newSearchTerm=SearchTerm(name=query)
        newSearchTerm.count=1
        newSearchTerm.save()

    #2.) The SearchBrowser
    #if the browser already exists in the database
    if SearchBrowser_exists == True:
        newSearchBrowser=SearchBrowser.objects.get(name=browser)
        #find the count
        count=newSearchBrowser.count
        #increase the count by 1
        count+=1
        newSearchBrowser.count=count
        newSearchBrowser.save()
    #if the browser does not exist yet
    elif  SearchBrowser_exists == False:
        newSearchBrowser=SearchBrowser(name=browser)
        newSearchBrowser.count=1
        newSearchBrowser.save()

