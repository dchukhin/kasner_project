from models import Search

def update_search_stats(query, browser):
    newSearchTerm=Search(name=query, browser=browser)
    #if the search term already exists
    if 1==2:
        aaa=1
    """
    @TODO:
    I think the best way to do it is to create a new table with the search
    term in it, then tell postgres to find the entry in the Search table 
    with the same name and increase its counter by 1.
    """
    #if the search term does not exist yet
    if (1==1):
        newSearchTerm.count=1
        newSearchTerm.save()
