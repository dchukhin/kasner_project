from django.shortcuts import render
from models import Keyword, Website

def index(request):
    return render(request, 'index.html')

def kasner(request):
    if 'query' in request.GET and request.GET['query']:
        q=request.GET['query']
        websites=Website.objects.filter(name__icontains=q)
        return render (request, 'results_page.html', 
                {'query' : q, 'websites' : websites})
    else:
        message='You did not search for anything! Try again.'
        return render (request, 'index.html', {'message': message})
