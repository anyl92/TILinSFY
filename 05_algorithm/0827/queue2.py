# 304
candy = 20
N = 50
per_list = [0] * N
Q = [0] * N
front = rear = -1

def isEmpty():
    return front == rear
def isFull():
    return (rear+1) % len(Q) == front

def enQ(item):
    global candy
    global rear
    per_list[item] += 1
    candy -= per_list[item]
    Q[rear + 1] = item
    rear += 1
    if candy == 0:
        return item
    return candy

def deQ():
    global Q
    global rear
    global front
    res = Q[front + 1]
    front += 1
    rear += 1
    return 'res', res
print(Q)
print(enQ(1))
print(deQ())

print(enQ(1))
print(enQ(2))

print(deQ())
print(enQ(1))
print(enQ(3))

print(deQ())
print(enQ(2))
print(enQ(4))

print(deQ())
print(enQ(1))
print(enQ(5))

print(deQ())
print(Q)