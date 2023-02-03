"""Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""."""

userInput = input("Please input a string. ") # gets user input

inputLength = len(userInput) # checks length of user input
splitInput = list(userInput) # splits user input into a list of each letter

checkMiddle = inputLength / 2 # divides length of user input by two


if checkMiddle.is_integer() == False: # checks if user input length is a whole number
    middleIndex = int(checkMiddle - 0.5) # if not , subtracts 0.5 from input length
    print(f"{splitInput[middleIndex]} is the middle letter of {userInput}") # prints the letter at index input length - 0.5
else:
    print("No middle letter") # if a whole number , prints no middle letter
