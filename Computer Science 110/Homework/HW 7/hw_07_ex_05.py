# hw_07_ex_05

def sum_list(l):
    '''Return the sum of all the elements in a list up to but not including
the first even number'''
    sum_accu = 0
    for i in l:
        if not(i % 2 == 0):
            sum_accu += i
        else:
            break
    return sum_accu

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
    test(sum_list([1,7,9,4,5]) == 17)
    test(sum_list([1,3,2,5,7]) == 4)
    test(sum_list([2,3,3,3,3]) == 0)
    test(sum_list([3,5,7,9,11]) == 35)  # No even number
    test(sum_list([]) == 0)

test_suite()

##Test at line 28 ok.
##Test at line 29 ok.
##Test at line 30 ok.
##Test at line 31 ok.
##Test at line 32 ok.
##>>> 
