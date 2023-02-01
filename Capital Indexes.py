
userInput = input("Please input a string. ")  # gets user input
upperValues = []  # creates an empty list to store the placement of each uppercase letter

for i in range (0, len(userInput)):  # runs program for the length of the user input
    if userInput[i].isupper():  # checks if each letter is uppercase
        upperValues.append(i)  # if uppercase, appends the index of the letter to upperValues

if len(upperValues) > 0:
    print(f"{userInput} contains uppercase characters at {upperValues}")  # prints the placement of the uppercase letters
else:
    print(f"'{userInput}' does not contain any uppercase letters.")
