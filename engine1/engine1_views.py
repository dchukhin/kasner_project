from django.shortcuts import render
from models import Keyword, Website
from django.template import RequestContext

from models import Website, Keyword

from stl_converter import stl
from blank_space_remover import bsr

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

def add_form(request):
    return render(request, 'add_form.html')

def add(request):
    if 'name' in request.POST and request.POST['name']:
        name=request.POST['name']
        url=request.POST['url']
        number=request.POST['number']
        keywords=request.POST['words']
        references=request.POST['references']
        referenced_by=request.POST['referenced_by']

        #if the website already exists, then we update it. Otherwise,
        #we create a new one
        w1=Website.objects.filter(url=url)
        if w1!=[]:
            w1.name=name
            w1.number=number
        #I decided to delete previous keywords, references, and referenced_by
        #elements, rather than going through each one and seeing if it is
        #in the db. Now, we will add each of these. This implies that each time
        #we use this form to update a website in the db we should be sending
        #all of the information to the db, which is what a web crawler would
        #be doing.
            w1.delete()
        #actually, later, I am planning on writing code to just update
        #a website, rather than deleting it and creating a new one
        w1=Website(name=name, url=url, number=number)
        w1.save()        

        #remove blank spaces from words, references, and referenced_by 
        #and separate into separate entries in a list, rather than just
        #a string
        keywords=stl(keywords)
        references=stl(references)
        referenced_by=stl(referenced_by)

        #add the keywords that describe this Website
        for keyword in keywords:
            #if keyword already exists, then we find it and name it k1. 
            #Otherwise, we create a new Keyword
            try:
                k1=Keyword.objects.get(name=keyword)
                w1.words.add(k1)
            except Keyword.DoesNotExist:
                #create the new Keyword and save it
                k1=Keyword(name=keyword)
                k1.save()
                #add this word to the Website
                w1.words.add(k1)        
        """
        @TODO:
        #add the references from the website
        """
        return render(request, 'add_form.html',
                    context_instance=RequestContext(request))

    else:
        return render(request, 'add_form.html', 
            context_instance=RequestContext(request))
