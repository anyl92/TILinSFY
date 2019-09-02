from collections import deque

dq = deque([])

def enque(x):
    if len(dq) == 0:
        dq.append(x)
    else:
        for i in range(len(dq)):
            if dq[i] > x:
                dq.insert(i, x)
                break
        if i not in dq:
            dq.append(x)

enque(1)
enque(5)
enque(2)
enque(4)
enque(3)

print(dq)