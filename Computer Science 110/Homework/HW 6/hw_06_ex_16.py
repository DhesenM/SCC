# hw_06_ex_16

def is_factor(f,n):
    '''Reture True if f is a factor of n, and return False if f is not
a factor of n.'''
    if n % f == 0:
        return True
    else:
        return False
    
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
    test(is_factor(3,12))
    test(not is_factor(5,12))
    test(is_factor(7,14))
    test(not is_factor(7,15))
    test(is_factor(1,15))
    test(is_factor(15,15))
    test(not is_factor(25,15))

test_suite()

##Test at line 25 ok.
##Test at line 26 ok.
##Test at line 27 ok.
##Test at line 28 ok.
##Test at line 29 ok.
##Test at line 30 ok.
##Test at line 31 ok.
##>>> 
