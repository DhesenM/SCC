def isEven(n):
    if n % 2 == 0:
        return True
    elif n % 2 == 1:
        return False
    else:
        a = "n is not an integer."
        return a

def isOdd(n):
    if isEven(n) == True:
        return False
    elif isEven(n) == False:
        return True
    else:
        a = "n is not an integer."
        return a


