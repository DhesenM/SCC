# hw_08_ex_03

##Encapsulate
##fruit = "banana"
##count = 0
##for char in fruit:
##    if char == "a":
##        count += 1
##print(count)

def count_letters(string,letter):
    '''Return the number of characters, rather than print the answer.'''
    counter = 0
    for char in string:
        if char == letter:
            counter += 1
    return counter

# test
##print(count_letters("banana","a"))
##3
##>>> 
