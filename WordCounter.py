
runProgram = True

print("Hello and welcome to the title word counter checker.")

while runProgram == True:
    startProgram = input("Would you like to check if the word count of your book title is good for marketing? (yes/no) ").lower()
    if startProgram == "yes":
        title = input("Please input your book title. ")
        titleLength = len(title.split())
        print(f"Your book title contains {titleLength} words")
        if titleLength <= 2:
            print("Your book has good marketability! Congratulations! ")
        else:
            print("Your book title is too long. Try shortening it for better marketability. ")
    else:
        print("Thank you for using this program.")
        runProgram = False

