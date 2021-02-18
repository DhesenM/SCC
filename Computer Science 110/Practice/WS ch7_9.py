#WS ch7_9

##def fruitVendor():
##    fruit_vendor = [("apple",250,1.25),("peach",100,0.95),("banana",75,0.2),
##                ("orange",125,0.5)]
##    number_1 = 0
##    number_2 = 0
##    value = 0
##    for (nm,num,val) in fruit_vendor:
##        number_1 += num
##        value += num * val
##        ave_cost = round(value / number_1, 3)
##    for (nm,num,val) in fruit_vendor:
##        if val > ave_cost:
##            number_2 += 1
##
##    print("The total number of pieces of fruit is {}.\n".format(number_1) +
##          "The total value for the fruit is {}.\n".format(value) +
##          "The average cost of a piece of fruit is {}.\n".format(ave_cost)+
##          "The number of pieces of fruit that have a greater than average cost is {}.".format(number_2))
##
##fruitVendor()
##
####The total number of pieces of fruit is 550.
####The total value for the fruit is 485.0.
####The average cost of a piece of fruit is 0.882.
####The number of pieces of fruit that have a greater than average cost is 2.
####>>> 


#WS ch7_10

##def sqrt(n):
##    guess = n/2
##    while True:
##        root = (guess + n/guess)/2
##        if abs(guess - root) < 0.0001:
##            return guess
##        guess = root
##
##print(sqrt(25))


#WS ch7_11

##def GL():
##    import math
##    n = 0
##    sum_accu = 0
##    while True:
##        n += 1
##        a = 1/(2*n-1)
##        if n % 2 == 1:
##            sum_accu += a
##        else:
##            sum_accu -= a
##        if abs(sum_accu - math.pi/4) < 0.001:
##            return n
##
##print(GL())
