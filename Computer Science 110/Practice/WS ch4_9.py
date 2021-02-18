def factorial(n):
    prod_accu = 1
    for i in range(1,n+1):
        prod_accu *= i
    return prod_accu

def e_to_the_x_series(x,n):
    ex = 1
    sum_accu = 1
    for i in range(n):
        e = (x**sum_accu)/factorial(sum_accu)
        ex += e
        sum_accu += 1
    return ex

import math
x = 0
for i in range(11):
    print(x,'     ',round(e_to_the_x_series(x,10),4),'     ',round((math.e)**x,4))
    x += 0.5
    
        
