stack = [None for index in range(0,10)]
basePointer = 0
topPointer = -1
stackFull = 10
item = None

def pop():
    global topPointer, basePointer, item
    if topPointer == basePointer -1:
        print("Stack is empty,cannot pop")
    else:
        item = stack[topPointer]
        topPointer = topPointer -1
        print("Poping ", item)
        print("Now, ", item, " is garbage data.")
        print("Stack: \t", stack)

def push(item):
    global topPointer
    if topPointer < stackFull - 1:
        topPointer = topPointer + 1
        stack[topPointer] = item
        print("Stack: \t", stack)
    else:
        print("Stack is full, cannot push")

push(7)
push(32)
pop()
pop()
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
push(9)
push(10)
push(11)
