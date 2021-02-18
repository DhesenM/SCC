# hw_08_ex_02

##Modify
##prefixes = "JKLMNOPQ"
##suffix = "ack"
##
##for letter in prefixes:
##    print(letter + suffix)

prefixes = "JKLMNOPQ"

for letter in prefixes:
    suffix = "ack"
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    print(letter + suffix)

##Jack
##Kack
##Lack
##Mack
##Nack
##Ouack
##Pack
##Quack
##>>> 
