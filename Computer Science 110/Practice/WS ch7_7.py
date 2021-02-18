# WS ch7_7

##def num_digits(n):
##    count = 0
##    while n != 0:
##        count += 1
##        n = n // 10
##    return count


# WS ch7_8

def guessNum():
    import random
    rng = random.Random()
    number = rng.randint(1,128)

    score = 100
    guesses = 0
    msg = ""

    while True:
        guess = int(input(msg + "\nGuess my number between 1 and 128: "))
        guesses += 1
        if guess > number:
            score -= 2
            msg += str(guess) + " is too high.\n"
        elif guess < number:
            score -= 2
            msg += str(guess) + " is too low.\n"
        else:
            if guesses == 1:
                print("Congratulations!")
            print("The secret number is {}.\nYou got it in {} guesses.\nYour final score is {}.".format(number,guesses,score))
            break

guessNum()
    
