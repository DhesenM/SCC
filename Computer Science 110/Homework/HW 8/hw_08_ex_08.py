# hw_08_ex_08

def reverse(string):
    '''Return the reverse the given string'''
    n = len(string)
    word = ''
    for i in range(n):
        word += string[n-1-i:n-i]
    return word

def mirror(string):
    '''Return the mirror of the given string'''
    word = string + reverse(string)
    return word
    
#test
import sys
def test(did_pass):
    '''Print the result of a test.'''
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAIlED.".format(linenum))
    print(msg)

def test_suite():
    '''Run the suite of tests for code in this module (this file).'''
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")

test_suite()
##Test at line 29 ok.
##Test at line 30 ok.
##Test at line 31 ok.
##Test at line 32 ok.
##>>> 
