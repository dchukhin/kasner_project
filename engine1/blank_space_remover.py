#/bin/python

#blank space remover removes blank spaces from the beginning & end of word
def bsr(word):
    #if the word is blank, return blank word back
    if word=='':
        return word
    #if the word starts with blank character(s), then we go through the blank
    #characters until the first non blank character
    if word[0]==' ':
        for j in range (0,len(word)):
            if word[j]==' ':
                #if we're at end of word and character==' ':
                if j==len(word)-1:
                    word=''
                    return ''
                pass
            elif word[j]!=' ':
                word=word[j:len(word)]
                break
            j=j+1
    #if the word ends with blank character(s), we work backwards until the
    # first non blank character
    if word[len(word)-1]== ' ':
        for j in range(0,len(word)):
            #if the last letter is blank
            if word[len(word)-j-1]==' ':
                pass
            elif word[len(word)-j-1]!=' ':
                word=word[0:len(word)-j]
                break
            j=j+1
    #if the word doesn't start or end in a blank character
    else:
        word=word
    return word

