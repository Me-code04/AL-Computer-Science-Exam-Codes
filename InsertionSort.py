# Insertion sort
myList = [12,13,11,5,6]

def InsertionSort (arrList):
    for index in range(len(arrList)):
        #print(index)
        key = arrList[index]
        place = index - 1
        if key < arrList[place]:
            while (place >= 0) and (key < arrList[place]):
                temp = arrList[place + 1]
                arrList[place + 1] = arrList[place]
                arrList[place] = temp
                place = place - 1
        index = index + 1
    print(arrList)

InsertionSort (myList)
