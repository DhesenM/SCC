# hw_04_ex_07

def sum_to(n):
    '''Return the sum of all integer numbers up to and including n'''
    sum_accu = 0
    for i in range(1,n+1):  
        sum_accu += i         # 1+2+3+...+n
    return sum_accu

# test
print("Sum of all integer numbers up to and including 10 is",sum_to(10))

##Sum of all integer numbers up to and including 10 is 55
##>>> 
