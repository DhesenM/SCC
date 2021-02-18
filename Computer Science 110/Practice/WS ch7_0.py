#WS ch7_0

##def condition(n):
##    if n % 7 == 0 and not(n % 5 == 0):
##        return True
##    else:
##        return False
##
##def ch7_0():
##    counter = 0
##    for i in range(1,501):
##        if condition(i):
##            counter += 1
##    return counter
##
##print(ch7_0())

##57
##>>>


#WS ch7_1

##def sum_of_odds(n):
##    sum_of_odds = n**2
##    return sum_of_odds

##def sum_of_odds(n):
##    sum_accu = 0
##    for i in range(1,n+1):
##        if i % 2 == 1:
##            sum_accu += i
##    return sum_accu


#WS ch7_2

##def sum_of_odds_1(a,b):
##    s_a = sum_of_odds(a-1)
##    s_b = sum_of_odds(b)
##    s_ab = s_b - s_a
##    return s_ab

##def sum_of_odds_1(a,b):
##    sum_accu = 0
##    for i in range(a,b+1):
##        if i % 2 == 1:
##            sum_accu += i
##    return sum_accu
##
##print(sum_of_odds_1(3,7))


#WS ch7_3


##import turtle
##sc = turtle.Screen()
##t = turtle.Turtle()
##d = turtle.Turtle()

##def randint(n1,n2):
##    import random
##    r = random.randint(n1,n2+1)
##    return r
##
##def ran_walk(t,Dz,n):
##    for i in range(n):
##        t.lt(randint(0,360))
##        t.fd(Dz)
        

#WS ch7_4

##def randint(n1,n2):
##    import random
##    r = random.randint(n1,n2)
##    return r
##
##def draw_circle(R):
##    d = turtle.Turtle()
##    d.pu()
##    d.goto(0,-R)
##    d.pd()
##    d.circle(R)
##
##def stop_when_circle_xd(t,Dz,R):
##    draw_circle(R)
##    counter = 0
##    x,y =0,0
##    while x**2 + y**2 < R**2:
##        t.lt(randint(0,360))
##        t.fd(Dz)
##        x,y = t.pos()
##        counter += 1
##    return counter
##
##print(stop_when_circle_xd(t,30,100))


#WS ch7_5

##def seq3n(n):
##    l = [n]
##    while n != 1:
##        if n % 2 == 0:
##            n = n // 2
##            l.append(n)
##        else:
##            n = 3 * n + 1
##            l.append(n)
##    return l
##
##
###WS ch7_6
##
##
##def longest():
##    i = 3
##    while i <= 1000:
##        a = len(seq3n(i))
##        b = len(seq3n(2))
##        if a <= b:
##            i += 1
##        else:
##            b = a
##            i += 1
##    return b
##
##print(longest())


#WS ch7_7
    
            
            
            
            
        

