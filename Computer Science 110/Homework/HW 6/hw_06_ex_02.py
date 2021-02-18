# hw_06_ex_02

def day_name(num):
    '''Return an integer number 0 to 6 into the name of a day.
Return None if the arguments to the function are not calid.'''
    if num == 0:
        return "Sunday"
    elif num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
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
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

test_suite()

##Test at line 37 ok.
##Test at line 38 ok.
##Test at line 39 ok.
##>>> 
