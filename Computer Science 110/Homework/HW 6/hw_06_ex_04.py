# hw_06_ex_04

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
        num = 1
    elif name == "Tuesday":
        num = 2
    elif name == "Wednesday":
        num = 3
    elif name == "Thursday":
        num = 4
    elif name == "Friday":
        num = 5
    elif name == "Saturday":
        num = 6
    elif name == "Sunday":
        num = 0
    else:
        num = None
    return num

def day_add(name,num):
    '''Return the resulting day name of the given day name and the number
of days'''
    return_day = (day_num(name) + num) % 7
    return_day_name = day_name(return_day)
    return return_day_name


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
    test(day_add("Monday",4) == "Friday")
    test(day_add("Tuesday",0) == "Tuesday")
    test(day_add("Tuesday",14) == "Tuesday")
    test(day_add("Sunday",100) == "Tuesday")
    
test_suite()    

##Test at line 65 ok.
##Test at line 66 ok.
##Test at line 67 ok.
##Test at line 68 ok.
##>>> 
