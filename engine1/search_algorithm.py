from django.shortcuts import render
from models import Keyword, Website


def algorithm(request):
    q=request.GET['query']
    #1.) search for websites whose names match query exactly (case insensitive)
    name_matches=Website.objects.filter(name__iexact=q)
    websites=list(name_matches)

    #2.) search for the wikipedia matches for the query
    wikipedia_search='wikipedia.org/wiki/'+q
    wikipedia_site=Website(name='Wikipedia Results', url=wikipedia_search)
    wikipedia_matches=wikipedia_site
    websites.append(wikipedia_matches)

    #3.) search for facebook matches
    facebook_search='www.facebook.com/public/'+q
    facebook_site=Website(name='Facebook results', url=facebook_search)
    facebook_matches=facebook_site  
    websites.append(facebook_matches)

    return websites



