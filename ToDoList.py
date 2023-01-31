runProgram = True
print("Welcome to my book title counter!")

while runProgram == True:
    startProgram = input("Would you like me to count the letters in the title of your book? (yes/no) ").lower()
    if startProgram == "yes":
        # get user input as variable 'title'

        title = input("Please input the title of your book. ")

        # store length of 'title' as 'titleLength'

        titleNoSpace = title.replace(" ", "")
        titleLength = len(titleNoSpace)

        print(f"There are {str(titleLength)} letters in {title}, not including spaces")
    else:
        print("Thank you for using this program!")
        runProgram = False

