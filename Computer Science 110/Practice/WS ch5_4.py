for i in range(2,251):
    if i % 7 == 0:
        if not(i % 3 == 0) and not(i % 5 == 0):
            print(i,"is divisible by 7 but not divisible by 3 or 5")
