def sqrt(num):
    if num == 1 or num == 0:
        return num
    
    maxGuess = num

    minGuess = 1 if num > 1 else num
    maxGuess = num if num > 1 else 1
    guess = None

    for x in range(100):
        guess = (minGuess+maxGuess)/2
        if guess*guess == num:
             return guess
        elif guess*guess > num:
             maxGuess = guess
        else:
             minGuess = guess

    return guess

print(sqrt(6.25))
    