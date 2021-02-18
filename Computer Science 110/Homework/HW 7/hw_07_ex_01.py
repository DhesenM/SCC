# hw_07_ex_01

def count_odd_number(l):
    '''Return the number of odd numbers in the list l'''
    counter = 0
    for i in l:
        if type(i) == int and i % 2 == 1:
            counter += 1
    return counter

# test
a = [1,3,4,7.5,9,"9"]
print(count_odd_number(a))

##3
##>>> 
