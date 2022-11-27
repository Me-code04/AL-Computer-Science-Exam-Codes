myList = [70, 46, 43, 27, 57, 41, 45, 21, 14]
lowerBound = 0
upperBound = len(myList)

for index in range(lowerBound + 1, upperBound):
    key = myList[index]
    place = index - 1
    if myList[place] > key:
        while place >= lowerBound and myList[place] > key:
            temp = myList[place +1]
            myList[place +1] = myList[place]
            myList[place] = temp
            place -= 1
        myList[place +1] = key
        print(myList)

print("Sorted List:\t",myList)
