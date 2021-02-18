# hw_06_ex_01

def turn_clockwise(cps):
    '''Return the next compass point in the clockwise direction'''
    if cps == "N":
        return "E"
    elif cps == "E":
        return "S"
    elif cps == "S":
        return "W"
    elif cps == "W":
        return "N"
    else:
        return None

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
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

test_suite()

##Test at line 30 ok.
##Test at line 31 ok.
##Test at line 32 ok.
##Test at line 33 ok.
##>>> 
