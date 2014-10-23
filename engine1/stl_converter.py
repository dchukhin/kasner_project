#/bin/python
from blank_space_remover import bsr

def stl(string):
    #set i=0, make a loop run until it gets to the end of the string
    i=0
    our_list=[]
    new_word=''
    while i<len(string):
        #if we get to a comma, add whatever was before to the list
        if string[i] == ',':
            #remove blank spaces
            new_word=bsr(new_word)
            #if new word is: '', then we shouldn't add it to the list
            if new_word=='':
                pass
            else:
                our_list.append(new_word)
                new_word=''
        else:
            new_word=new_word + string[i]
            #if we got to the end of the string, add the last part to the list
            if i==len(string)-1:
                new_word=bsr(new_word)
                our_list.append(new_word)
        i=i+1
    return our_list
