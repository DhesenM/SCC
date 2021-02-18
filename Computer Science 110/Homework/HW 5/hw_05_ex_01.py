# hw_05_ex_01

def dayname(num):
    '''Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to
Saturday. Return the day name of the given number. '''
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
        return "Error"

# test
print(dayname(2))
print(dayname(7))

##Tuesday
##Error
##>>> 
