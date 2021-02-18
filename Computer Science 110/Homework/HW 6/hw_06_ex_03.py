# hw_06_ex_03

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

def day_num(name):
    '''Return the number of the given day name'''
    if name == "Monday":
        a = 1
    elif name == "Tuesday":
        a = 2
    elif name == "Wednesday":
        a = 3
    elif name == "Thursday":
        a = 4
    elif name == "Friday":
        a = 5
    elif name == "Saturday":
        a = 6
    elif name == "Sunday":
        a = 0
    else:
        a = None
    return a

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
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)

test_suite()

##Test at line 57 ok.
##Test at line 58 ok.
##Test at line 59 ok.
##Test at line 60 ok.
##Test at line 61 ok.
##>>> 
