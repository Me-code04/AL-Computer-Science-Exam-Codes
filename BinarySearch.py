#Array declared
myList = [16,19,21,27,36,42,55,67,76,89]

#Variables declared
upperBound = len(myList) - 1
lowerBound = 0
item = int(input("Please enter item to be found: "))
found = False

#Binary search
while (found == False) and (lowerBound <= upperBound):
    index = (lowerBound + upperBound)//2
    if myList[index] == item:
        found = True    
    if item > myList[index]:
        lowerBound = index + 1
    if item < myList[index]:
        upperBound = index - 1

#Output
if found:
    print("Item found")
else:
    print("Item not found")
