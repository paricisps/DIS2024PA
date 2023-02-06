import random  # imports random function

unsolved = True  # variable stores whether the number has been solved or not
guessNo = 0  # store the number of guesses
num = random.randint(0,100)  # generates a random number at the beginning and stores it in num

totalSolved = 0
solveNo = []

impossible = 0
quick = 0
average = 0
slow = 0
long = 0

while unsolved:  # runs loop while number is unsolved
    guess = int(input("Please guess a number between 0 and 100."))  # takes the users guess
    guessNo += 1  # adds +1 to the guess counter
    if guess > num:  # runs is guess is bigger than the number
        print(f"The number is smaller than {guess}")
    elif guess < num:  # runs if guess is smaller than the number
        print(f"The number is bigger than {guess}")
    elif guess == num:  # runs if guess is equal to the number
        print(f"Congratulations! The number was {num}. You guessed it in {guessNo} tries.")
        totalSolved += 1
        solveNo.append(guessNo)
        playAgain = input("Would you like to play again? y/n ").lower()  # checks if user would like to play again

        if playAgain == "y":  # runs if player would like to play again
            guessNo = 0  # resets guess counter
            num = random.randint(0, 100)  # randomly chooses a new number
        else:  # runs if player does not want to play again
            unsolved = False  # sets unsolved to false

            for i in solveNo:
                if i == 1:
                    impossible += 1
                elif i < 5:
                    quick += 1
                elif i < 10:
                    average += 1
                elif i < 15:
                    average += 1
                else:
                    long += 1

            print("Thank you for playing!")  # thanks user

            print(f"You solved {totalSolved} numbers.")

            print(f"{(impossible/ totalSolved)*100}% were solved in one guess.")
            print(f"{(quick / totalSolved) * 100}% were solved quickly.")
            print(f"{(average / totalSolved) * 100}% were solved at an average speed.")
            print(f"{(slow / totalSolved) * 100}% were solved slowly.")
            print(f"{(long / totalSolved) * 100}% took you way too long to solve.")
