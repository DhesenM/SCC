# hw_05_ex_02

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

def day_week(num_start,length_stay):
    '''Ask for the starting day number and the length of your stay.
Return the name of day of the week you will return on.'''
    week_num = length_stay // 7   # Calculate the weeks you've gone
    day_left = length_stay % 7    # Calculate the days left 
    return_day = (num_start + day_left) % 7
# Calculate the returned name of the day
    print("The",dayname(return_day),"of the week",week_num,"you will return.")

# test
day_week(3,137)

##The Sunday of the week 19 you will return.
##>>> 
    
