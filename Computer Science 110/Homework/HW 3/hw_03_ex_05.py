## hw_03_ex_05

##(a) Write a loop that prints each of the numbers on a new line.

for i in (12,10,32,3,66,17,42,99,20):
    print(i)

## Dividing Line
print("------------")

##(b) Write a loop that prints each number and its square on a new line.

for i in (12,10,32,3,66,17,42,99,20):
    print(i,"    ",i**2)

## Dividing Line
print("------------")

##(c) Write a loop that adds all the numbers from the list into a variavle
## called total. You should set the total variavle to have the value 0 before
## you start adding them up, and print the value in total after the loop
## has completed.

total = 0
for i in (12,10,32,3,66,17,42,99,20):
    total += i
print("The value of all the numbers in the list is " + str(total) + ".")

## Dividing Line
print("------------")

##(d) Print the product of all the numbers in the list. (product means all
## multiplied together)

prod_accu = 1
for i in (12,10,32,3,66,17,42,99,20):
    prod_accu *= i
print("The product of all the numbers in the list is " + str(prod_accu) + ".")

##12
##10
##32
##3
##66
##17
##42
##99
##20
##------------
##12      144
##10      100
##32      1024
##3      9
##66      4356
##17      289
##42      1764
##99      9801
##20      400
##------------
##The value of all the numbers in the list is 301.
##------------
##The product of all the numbers in the list is 1074879590400.
##>>>
