def find_browser(request):
    """
    Returns the browser name.

    Function is used to determine which CSS to load for each page. CSS should 
    match the browser. For unknown browsers we return 'unknown' and use the 
    CSS for unknown browsers.
    """
    #get the META data about the browser type
    browser=request.META['HTTP_USER_AGENT']
    #make META data all lowercase
    browser=browser.lower()
    #for firefox
    if 'firefox' in browser:
        browser='firefox'
    #for chrome
    elif 'chrome' in browser:
        browser='chrome'
    #for all others
    else:
        browser='unknown'

    return browser
