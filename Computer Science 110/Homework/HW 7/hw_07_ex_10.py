# hw_07_ex_10

def is_prime(n):
    '''Return True when n is a prime number and False otherwise'''
    for i in range(2,n):
        if n % i == 0 or n == 1:
            return False
    return True



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
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(is_prime(20010401))  # My birthday

test_suite()

##Test at line 26 ok.
##Test at line 27 ok.
##Test at line 28 ok.
##Test at line 29 FAIlED.
##>>> 

# I was not born on a prime day.

def born_on_prime():
    '''Estimate the number of students who has a prime birth date
in a class of 100 students'''
    import random
    counter = 0
    for i in range(100):
        year = random.randint(1996,2001)
        month = random.randint(1,12)
        if (month % 2 == 1 and month < 8) or (month % 2 == 0 and month >= 8):
            day = random.randint(1,31)
        elif month == 2:
            if year % 4 == 0:
                day = random.randint(1,29)
            else:
                day = random.randint(1,28)
        else:
            day = random.randint(1,30)
        birth_date = int(str(year) + str(month) + str(day))
        if is_prime(birth_date):
            counter += 1
    return counter

def reduce_error():
    '''Make the result from born_on_prime more precise'''
    sum_accu = 0
    counter = 0
    for i in range(10):        # Reduce errors
        counter += 1
        sum_accu += born_on_prime()
    students_born_on_prime = sum_accu // counter
    return students_born_on_prime

print("The number of students who has a prime birth date in a class"
      " of 100 students is " + str(reduce_error()) + ".")

##The number of students who has a prime birth date in a class of 100 students is 7.
##>>> 


