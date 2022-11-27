#Linked List initialisation
myLinkedList = [None for index in range(0,11)]
myLinkedListPointers = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11, -1]
startPointer = -1
heapStartPointer = 0

# FUNCTION Find for data in Linked List 
def find(itemSearch):
    found = False
    itemPointer = startPointer
    while itemPointer != -1 and not found:
        if myLinkedList[itemPointer] == itemSearch:
            found = True
        else:
            itemPointer = myLinkedListPointers[itemPointer]
    return itemPointer

# PROCEDURE Insert data into the Linked List
def insert(itemAdd):
    global startPointer, heapStartPointer
    if heapStartPointer == -1:
        print("Linked List full")
    else:
        tempPointer = startPointer
        startPointer = heapStartPointer
        heapStartPointer = myLinkedListPointers[heapStartPointer]
        myLinkedList[startPointer] = itemAdd
        myLinkedListPointers[startPointer] = tempPointer
        print(myLinkedList, "\n", myLinkedListPointers)

# PROCEDURE Delete data from the linked list by searching
def delete(itemDelete):
    global startPointer, heapStartPointer
    if startPointer == -1:
        print("Linked List empty")
    else:
        index = startPointer
        while myLinkedList[index] != itemDelete and index != -1:
            oldindex = index
            index = myLinkedListPointers[index]
        if index == -1:
            print("Item ", itemDelete, " not found")
        else:
            myLinkedList[index] = None
            tempPointer = myLinkedListPointers[index]
            myLinkedListPointers[index] = heapStartPointer
            heapStartPointer = index
            myLinkedListPointers[oldindex] = tempPointer
    print(myLinkedList, "\n", myLinkedListPointers)

#Main Program
insert(18)
insert(2)
insert(36)
insert(1)
insert(3)
insert(20)

delete(36)

##enter item to search for
item = int(input("Please enter item to be found "))
result = find(item)
if result != -1:
    print("Item found")
else:
    print("Item not found")



