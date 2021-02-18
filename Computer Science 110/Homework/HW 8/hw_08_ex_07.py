# hw_08_ex_07

def reverse(string):
    '''Return the reverse the given string'''
    n = len(string)
    word = ''
    for i in range(n):
        word += string[n-1-i:n-i]
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
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    
test_suite()
##Test at line 24 ok.
##Test at line 25 ok.
##Test at line 26 ok.
##Test at line 27 ok.
##>>> 
