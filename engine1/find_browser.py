def find_browser(request):
    """
    Returns the browser name.

    Function is used to determine which CSS to load for each page. CSS should 
    match the browser. For unknown browsers we return 'firefox' and use the 
    CSS for firefox.
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
    #for all others we use same as for firefox
    else:
        browser='firefox'

    return browser
