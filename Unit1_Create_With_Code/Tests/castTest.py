difi = int(input("What difficult would you like? 0 (practise mode), 1, 2 or 3 (hardest) "))

match difi:
    case 0:
        guessLimit = 1000
        guesses = 0
    case 1:
        guessLimit = 7
        guesses = 0
    case 2:
        guessLimit = 6
        guesses = 0
    case 3:
        guessLimit = 5
        guesses = 0
    case '':
        guesses = 0
print(guessLimit)