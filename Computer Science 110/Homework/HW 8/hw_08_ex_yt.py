# Youtube link:http://youtu.be/21XGGIH3tvM?hd=1

# hw_08_ex_yt

def reverse(string):
    '''Return the reverse of the given string'''
    n = len(string)
    word = ''
    for i in range(n):
        word += string[n-1-i:n-i]
    return word

def rev_each_word_in(Sentence):
    '''Take a sentence of words that may or may not have a final period & which
returns a sentence, each of word of which is reversed.'''
    l = ''
    for word in Sentence.split():            
        rev_word = reverse(word)
        if '.' in rev_word:
            rev_word = rev_word.replace('.','')
            rev_word += '.'
        l += rev_word + ' '
    return l

print(rev_each_word_in('to be or not to be that is the question'))
print(rev_each_word_in('to be or not to be that is the question.'))

##ot eb ro ton ot eb taht si eht noitseuq 
##ot eb ro ton ot eb taht si eht noitseuq. 
##>>> 
