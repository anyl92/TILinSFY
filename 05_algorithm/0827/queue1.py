Q = [0]*100
rear = -1
front = -1

def enQueue(item):
    global Q
    global rear
    Q[rear+1] = item
    rear += 1
    return Q
print(enQueue(1))
print(enQueue(2))
print(enQueue(3))

def deQueue():
    global Q
    global front
    global rear
    res = Q[front + 1]
    #Q[front+1] = 0
    front += 1
    rear += 1
    #print(res)
    return res

print(deQueue())
print(deQueue())
print(deQueue())

Q = [0]*10
f = r = -1
def isEmpty():
    return f==r
def isFull():
    return r == len(Q)-1