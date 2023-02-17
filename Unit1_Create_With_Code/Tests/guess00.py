## IMPORTS ##
import random  # imports random function
import time

## FILES ##
f = open("guessInfo.txt", "a")

## VARIABLES ##
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

## USER INPUT ##
user = input("Please input your name. ")

## FILE WRITING ##
f.write(f"\nPlayer: {user} \n")
f.write(time.ctime() + "\n" +"\n")

## MAIN PROGRAM LOOP ##
while unsolved:  # runs loop while number is unsolved

    guess = int(input("Please guess a number between 0 and 100. "))  # takes the users guess
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

        ## PLAY AGAIN LOOP ##
        if playAgain == "y":  # runs if player would like to play again
            guessNo = 0  # resets guess counter
            num = random.randint(0, 100)  # randomly chooses a new number
        else:  # runs if player does not want to play again
            unsolved = False  # sets unsolved to false

            ## STATISTICS GENERATION ##
            for i in solveNo:  # checks what category the solve time falls into
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
            print(f"{'~'*15} STATISTICS {'~'*15} ")
            print(f"You solved {totalSolved} number/s.")  # lists number of numbers solved

            ## STATISTICS CALCULATION ##
            totalImpossible = round(((impossible / totalSolved)*100),2)
            totalQuick = round(((quick / totalSolved) * 100), 2)
            totalAverage = round(((average / totalSolved) * 100), 2)
            totalSlow = round(((slow / totalSolved) * 100), 2)
            totalLong = round(((long / totalSolved) * 100), 2)

            ## STATISTICS VIEW ##
            print(f"{totalImpossible}% were solved in one guess.")
            print(f"{totalQuick}% were solved quickly.")
            print(f"{totalAverage}% were solved at an average speed.")
            print(f"{totalSlow}% were solved slowly.")
            print(f"{totalLong}% took you way too long to solve.")

            ## WRITE STATISTICS TO FILE ##
            f.write(f"Games played: {totalSolved}" + "\n")
            f.write(f"{totalImpossible}% were solved in one guess." + "\n")
            f.write(f"{totalQuick}% were solved quickly."+ "\n")
            f.write(f"{totalAverage}% were solved at an average speed."+ "\n")
            f.write(f"{totalSlow}% were solved slowly."+ "\n")
            f.write(f"{totalLong}% took you way too long to solve."+ "\n")


