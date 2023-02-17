names = ["Adam", "Bill", "Chris", "David", "Peyton"]

myname = "Peyton"
print(myname[:2])
for i, char in enumerate(myname):
    print(i+1, char)

for name in names:
    print(name)

print(type(names))

for index, name in enumerate(names):
    print(index , name)