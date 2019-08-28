Q = []
def Qinit():
    global Q
    Q.clear()

def Qisempty():
    global Q
    return len(Q) == 0

def enQ(value):
    Q.append(value)

def deQ():
    return Q.pop(0)

def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        Qinit()
        l = list(input().split())

        for i in l:
            enQ(i)

        while not Qisempty():
            value = deQ()
            if value != None:
                print(value, end=' ')
        print()
