from models import Keyword, Website
from stl_converter import stl

#This function is used to add records to the database by the web crawler.
def add(request):
    name=request.POST['name']
    url=request.POST['url']
    number=request.POST['number']
    keywords=request.POST['words']
    """
    If the website already exists, then we update it. Otherwise, we create 
    a new one.
    """
    w1=Website.objects.filter(url=url)
    """
    At this point, the previous entry for this website is deleted, rather than 
    updated. The idea is that it is faster to delete the old record, rather 
    than searching through each of its fields to check which ones need to be 
    updated and which do not.
    """
    if w1!=[]:
        w1.name=name
        w1.number=number
        w1.delete()
    #Now we add the website to the database.
    w1=Website(name=name, url=url, number=number)
    w1.save()
    """Remove blank spaces from words and separate into separate entries in 
    a list, rather than just a string.
    """   
    keywords=stl(keywords)
    """
    Add the keywords that describe this Website. If the keyword already 
    exists, then we find it and name it k1. Otherwise, we create a 
    new Keyword.
    """
    for keyword in keywords:
        try:
            k1=Keyword.objects.get(name=keyword)
            w1.words.add(k1)
        except Keyword.DoesNotExist:
            #Create the new Keyword and save it.
            k1=Keyword(name=keyword)
            k1.save()
            #add this word to the Website
            w1.words.add(k1)
