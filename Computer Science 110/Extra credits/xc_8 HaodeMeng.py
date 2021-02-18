# Youtube link:http://youtu.be/dsf-zyVMT4o?hd=1

# xc_8

import math

def isPrime(n):
    '''Return True if int n > 0 is a prime, OTW returns False.'''
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        if n % 2 == 0:
            return False
        else:
            for f in range(3,math.ceil((math.sqrt(n)))+1,2):
                if n % f == 0:
                    return False
            return True


# Q1
def twinPrimes(n):
    '''Print out the first n twin primes, 5 per line.'''
    counter,i = 0,1
    while True:
        if isPrime(i) and isPrime(i+2):
            print('{:>15}'.format('('+str(i)+','+str(i+2)+')'),end='')
            counter += 1
            if counter % 5 == 0:
                print('\n',end = '')
            if counter == n:
                break
        i += 1

twinPrimes(100)

##          (3,5)          (5,7)        (11,13)        (17,19)        (29,31)
##        (41,43)        (59,61)        (71,73)      (101,103)      (107,109)
##      (137,139)      (149,151)      (179,181)      (191,193)      (197,199)
##      (227,229)      (239,241)      (269,271)      (281,283)      (311,313)
##      (347,349)      (419,421)      (431,433)      (461,463)      (521,523)
##      (569,571)      (599,601)      (617,619)      (641,643)      (659,661)
##      (809,811)      (821,823)      (827,829)      (857,859)      (881,883)
##    (1019,1021)    (1031,1033)    (1049,1051)    (1061,1063)    (1091,1093)
##    (1151,1153)    (1229,1231)    (1277,1279)    (1289,1291)    (1301,1303)
##    (1319,1321)    (1427,1429)    (1451,1453)    (1481,1483)    (1487,1489)
##    (1607,1609)    (1619,1621)    (1667,1669)    (1697,1699)    (1721,1723)
##    (1787,1789)    (1871,1873)    (1877,1879)    (1931,1933)    (1949,1951)
##    (1997,1999)    (2027,2029)    (2081,2083)    (2087,2089)    (2111,2113)
##    (2129,2131)    (2141,2143)    (2237,2239)    (2267,2269)    (2309,2311)
##    (2339,2341)    (2381,2383)    (2549,2551)    (2591,2593)    (2657,2659)
##    (2687,2689)    (2711,2713)    (2729,2731)    (2789,2791)    (2801,2803)
##    (2969,2971)    (2999,3001)    (3119,3121)    (3167,3169)    (3251,3253)
##    (3257,3259)    (3299,3301)    (3329,3331)    (3359,3361)    (3371,3373)
##    (3389,3391)    (3461,3463)    (3467,3469)    (3527,3529)    (3539,3541)
##    (3557,3559)    (3581,3583)    (3671,3673)    (3767,3769)    (3821,3823)
##>>> 


#Q2
def sumOftwinPrimes(n):
    '''Return the first n sum of primes'''
    counter,i,sum_accu = 0,1,0
    while True:
        if isPrime(i) and isPrime(i+2):
            counter += 1
            sum_accu += (2*i+2)
            if counter == n:
                break
        i += 1
    return sum_accu
###test
##print(sumOftwinPrimes(2))
##20
##>>>

###The sum of first 100 twin primes.
print(sumOftwinPrimes(100))
##328184
##>>>


#Q3
###The sum of the first 50 twin primes divided by the sum of the 51th to the
###100th twin primes.
print(sumOftwinPrimes(50)/(sumOftwinPrimes(100)-sumOftwinPrimes(50)))
##0.23103468971311966
##>>> 


#Q4
def LargestGapOftwinPrimes(n):
    '''Return the largest gap of first n twin primes'''
    counter,i = 0,1
    currentb,currentc,largestGap = 5,5,2
    while True:
        if isPrime(i) and isPrime(i+2):
            counter += 1
            currentc = i
            currentGap = currentc - currentb
            currentb = i+2
            if largestGap < currentGap:
                largestGap = currentGap
            if counter == n:
                break
        i += 1
    return largestGap
###test
##print(LargestGapOftwinPrimes(7))
##16
##>>>

###The largest gap of the first 100 twin primes.
print(LargestGapOftwinPrimes(100))
##166
##>>> 
