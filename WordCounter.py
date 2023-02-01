runProgram = True #lets the loop run

print("Hello and welcome to the title word counter checker.") # greets the user
titleHistory = [] # creates list for books
lengthHistory = [] # creates list for title Length

while runProgram == True: # beginning of loop
    startProgram = input("Would you like to check if the word count of your book title is good for marketing? (yes/no) ").lower() # asks the user if they want to start

    if startProgram == "yes": # runs if user wants to start
        title = input("Please input your book title. ") #lets user input title

        titleLength = len(title.split()) # checks the number of words in the title

        titleHistory.append(title.title()) # appends the title name to list
        lengthHistory.append(titleLength) # appends the title length to list

        print(f"The title of your book, {title.title()} contains {titleLength} words") # prints the words in the title

        if titleLength <= 2: # checks if title is less than or equal to 2
            print("Your book has good marketability! Congratulations! ")

        else: # runs if title is more than 2
            print("Your book title is too long. Try shortening it for better marketability. ")

    else: # runs if user does not want to start program
        print("Thank you for using this program.")
        print(50 * '~')
        print("The books you checked were: ")

        for i in range(0, len(titleHistory)): # runs loop for the amount of entries in the titleHistory list
            print(f"{i+1}: {titleHistory[i]}, containing {lengthHistory[i]} words") # prints the title and its associated word length

        runProgram = False # stops the loop from running again, ending the program

