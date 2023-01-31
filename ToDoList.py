
#get user input as variable 'title'

title = input("Please input the title of your book. ")

#store length of 'title' as 'titleLength'

titleNoSpace = title.replace(" ", "")
titleLength = len(titleNoSpace)

print("There are " + str(titleLength) + " letters in " + title)
