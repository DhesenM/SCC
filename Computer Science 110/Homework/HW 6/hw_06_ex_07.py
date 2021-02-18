# hw_06_ex_07

def to_secs(hours,minutes,seconds):
    '''Return a total number of seconds of the given hours, minutes
and seconds'''
    ms = hours * 60
    ss = (ms + minutes) * 60
    total_seconds = ss + seconds
    return total_seconds

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
    test(to_secs(2,30,10) == 9010)
    test(to_secs(2,0,0) == 7200)
    test(to_secs(0,2,0) == 120)
    test(to_secs(0,0,42) == 42)
    test(to_secs(0,-10,10) == -590)
    
test_suite()

##Test at line 25 ok.
##Test at line 26 ok.
##Test at line 27 ok.
##Test at line 28 ok.
##Test at line 29 ok.
##>>> 
