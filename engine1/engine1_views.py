from django.shortcuts import render
from models import Keyword, Website
from django.template import RequestContext

from blank_space_remover import bsr
import add_to_db
import twitter_attempt1
from search_algorithm import algorithm
from find_browser import find_browser
from update_search_stats import update_search_stats
import write_search_stats

def index(request):
    browser=find_browser(request)
    return render(request, 'index.html', {'browser':browser})

def kasner(request):
    browser=find_browser(request)
    if 'query' in request.GET and request.GET['query']:
        q=request.GET['query']
        #update the search stats in db
        update_search_stats(q, browser)
        #use our search algorithm to get websites for results
        websites = algorithm(request)
        return render (request, 'results_page.html', 
                {'query' : q, 'websites' : websites, 'browser':browser})
    else:
        message='You did not search for anything! Try again.'
        return render (request, 'index.html', 
                {'message': message,'browser':browser})

def add_form(request):
    return render(request, 'add_form.html')

def add(request):
    if 'name' in request.POST and request.POST['name']:
        add_to_db.add(request)
        return render(request, 'add_form.html',
                    context_instance=RequestContext(request))

    else:
        return render(request, 'add_form.html', 
            context_instance=RequestContext(request))

def about(request):
    tweets = twitter_attempt1.search
    browser = find_browser(request)
    return render(request,'about.html',{'tweets':tweets, 'browser':browser})

def another_page(request):
    browser=find_browser(request)
    aaa=request.META['HTTP_USER_AGENT']
    return render(request, 'another_page.html', 
            {'browser': browser, 'aaa':aaa})

def search_stats(request):
    return render(request, 'search_stats.html')

def stats_tabs(request):
    return render(request, 'stats-tabs.html')

def stats_browsers(request):
    #Fetch current stats from DB and write a JSON file of them.
    write_search_stats.write('browsers','templates')
    return render(request, 'stats_browsers.json')

def stats_terms(request):
    #Fetch current stats form DB and write a JSON file of them.
    write_search_stats.write('search_terms', 'templates')
    return render(request, 'stats_terms.json')
