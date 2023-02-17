

myList = ["a", "b", "c"]
name = input("What is your name? ")
myList.append(name)
for item in myList:
    with open("myTextFile2.txt", "a") as file:
        file.write("\n")
        file.write(item)


with open("myTextFile2.txt", "r") as file:
    print(file.read())