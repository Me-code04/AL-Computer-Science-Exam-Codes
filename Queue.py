queue = [None for index in range(0,10)]
frontPointer = 0
rearPointer = -1
queueFull = 10
queueLength = 0
item = 0
def enQueue(item):
    global queueLength, rearPointer
    if queueLength < queueFull:
        if rearPointer < len(queue) - 1:
            rearPointer = rearPointer + 1
            queue[rearPointer] = item
        else:
            rearPointer = 0
            queueLength = queueLength + 1
            queue[rearPointer] = item
        print("Queue right now:\t", queue)
    else:
        print("Queue is full, cannot enqueue")

def deQueue(): #Has issues
    global queueLength, frontPointer, item
    if queueLength == 0:
        print("Queue is empty,cannot dequeue")
    else:
        queue[frontPointer] = None
        if frontPointer == len(queue) - 1:
            frontPointer = 0
        else:
            frontPointer = frontPointer + 1
        print("Queue right now:\t", queue)
    queueLength = queueLength -1
    
#Main Program
enQueue(7)
enQueue(32)
deQueue()
deQueue()
deQueue()
for item in range(1,12):
    enQueue(item)
