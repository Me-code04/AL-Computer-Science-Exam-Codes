#Python program for linear search
#create array to store all the numbers
myList = [4,2,8,17,9,3,7,12,34,21]
#enter item to search for
item = int(input("Please enter item to be found "))
found = False
index = 0
while index != len(myList):
    if myList[index] == item:
        found = True
    index += 1
if found:
    print("Item found")
else:
    print("Item not found")
        
