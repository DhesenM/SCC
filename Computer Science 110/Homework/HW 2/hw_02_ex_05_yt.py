# Youtube link: http://youtu.be/lflKON2Vz90?hd=1

# The formula for computing the final amount if one is earning compound interest
# on Wikipedia as A = P*(1+r/n)**(n*t)
# Where,
# P = principal amount (initial investment)
# r = annual nominal interest rate (as a decimal)
# n = number of times the interest is compounded per year
# t = number of years

# Write a Python program that assigns the principal amount of$10000 to variable
# P, assign to n the value 12, and assign to r the interest rate of 8%. Then
# have the problem prompt the user for the number of years t that the money will
# be compounded for. Calculate and print the final amount after t years.

P = 10000   # assign the principal amount of $10000 to variable P
n = 12      
r = 0.08    # assign the interest rate of 8%
t = int(input("Enter the number of years t that the money will be compounded for:"))
# prompt the user to enter the number of years

A = P*(1+r/n)**(n*t)
print("The final amount after "+str(t)+" year/years is "+str(A)+".")
# print out the final amount after t years
