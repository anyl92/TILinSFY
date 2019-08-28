# Insertion Sort
arr = []
num = 0


def insertionSort():
    global arr
    for i in range(1, num):
        temp = arr[i]
        j = i - 1

        while temp < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp


def printResult():
    for i in range(0, num):
        print(arr[i], end=' ')


def main():
    global arr, num
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        arr = [int(x) for x in input().split()]

        insertionSort()
        print("#%d" % test_case, end=' ')
        printResult()


# Quick Sort
arr = []
num = 0


def quick_sort(first, last):
    if first < last:
        pivot = first
        i = first
        j = last

        while i < j:
            while arr[i] <= arr[pivot] and i < last:
                i += 1
            while arr[j] > arr[pivot]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot], arr[j] = arr[j], arr[pivot]

        quick_sort(first, j - 1)
        quick_sort(j + 1, last)


def main():
    global arr, num
    T = int(input())

    for test_case in range(1, T + 1):
        num = int(input())
        arr = [int(x) for x in input().split()]

        quick_sort(0, num - 1)
        print("#%d" % test_case, end=' ')
        for j in range(0, num):
            print(arr[j], end=' ')
        print()


# Counting Sort
MAX_N = 100
MAX_DIGIT = 10

N = 0
arr = []
cnt = []
sortedArr = []


def calculateDigitNumber():
    global cnt
    for i in range(N):
        cnt[arr[i]] += 1

    for i in range(1, MAX_DIGIT + 1):
        cnt[i] = cnt[i - 1] + cnt[i]


def executeCountingSort():
    global cnt, sortedArr
    for i in range(N - 1, -1, -1):
        sortedArr[cnt[arr[i]] - 1] = arr[i]
        cnt[arr[i]] = cnt[arr[i]] - 1


def main():
    global N, arr, cnt, sortedArr
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        arr = [int(x) for x in input().split()]
        sortedArr = [int(0)] * N
        cnt = [int(0)] * 11

        calculateDigitNumber()
        executeCountingSort()

        print("#%d" % test_case, end=' ')
        for i in range(N):
            print("%d" % sortedArr[i], end=' ')

        print()


# Binary Search
def binarySearch(arr, low, high, target):
    if low > high:
        print("-1", end=' ')
        return

    mid = (low + high) // 2

    if target < arr[mid]:
        binarySearch(arr, low, mid - 1, target)
    elif arr[mid] < target:
        binarySearch(arr, mid + 1, high, target)
    else:
        print(mid, end=' ')
        return


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        print("#%d" % test_case, end=' ')
        M = int(input())
        N = int(input())

        arr = list(map(int, input().split()))
        targetvalue = list(map(int, input().split()))

        for idx in range(N):
            binarySearch(arr, 0, M - 1, targetvalue[idx])
        print()


# DFS Searching
def depthFirstSearch(v, depth):
    global maxEdge

    if v == end:
        if maxEdge < 0 or depth < maxEdge:
            maxEdge = depth
        return

    visit[v] = True

    for i in range(1, vertex + 1):
        if MAP[v][i] == 1 and visit[i] is False:
            depthFirstSearch(i, depth + 1)
            visit[i] = False


def main():
    global vertex, end, visit, MAP, maxEdge

    T = int(input())

    for test_case in range(1, T + 1):
        vertex, edge, start, end = map(int, input().split())
        MAP = [[0] * (vertex + 1) for _ in range(vertex + 1)]
        visit = [False] * (vertex + 1)
        for _ in range(edge):
            v1, v2 = map(int, input().split())
            MAP[v1][v2] = 1
        maxEdge = -1
        depthFirstSearch(start, 0)
        print("#%d %d" % (test_case, maxEdge))


# BFS Searching
class Queue:
    class Point:
        def __init__(self, y, x, c):
            self.y = y
            self.x = x
            self.c = c

    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.head = self.rear = 0

    def isEmpty(self):
        return self.head <= self.rear

    def enQueue(self, y, x, c):
        self.queue[self.head] = self.Point(y, x, c)
        self.head = self.head + 1

    def deQueue(self):
        if self.isEmpty():
            return None
        self.rear = self.rear + 1
        return self.queue[self.rear - 1]


def breadthFirstSearch():
    queue = Queue(row * column)
    queue.enQueue(0, 0, 0)
    MAP[0][0] = 0

    while queue.isEmpty() == False:
        p = queue.deQueue()

        if p.y == row - 1 and p.x == column - 1:
            return p.c

        if p.y + 1 < row and MAP[p.y + 1][p.x]:
            queue.enQueue(p.y + 1, p.x, p.c + 1)
            MAP[p.y + 1][p.x] = 0
        if p.x + 1 < column and MAP[p.y][p.x + 1]:
            queue.enQueue(p.y, p.x + 1, p.c + 1)
            MAP[p.y][p.x + 1] = 0
        if p.y - 1 >= 0 and MAP[p.y - 1][p.x] != 0:
            queue.enQueue(p.y - 1, p.x, p.c + 1)
            MAP[p.y - 1][p.x] = 0
        if p.x - 1 > 0 and MAP[p.y][p.x - 1] != 0:
            queue.enQueue(p.y, p.x - 1, p.c + 1)
            MAP[p.y][p.x - 1] = 0

    return -1


def main():
    global MAP, row, column
    T = int(input())

    for test_case in range(1, T + 1):
        row, column = map(int, input().split())
        MAP = [[int(num) for num in input().split()] for _ in range(row)]
        print("#%d %d" % (test_case, breadthFirstSearch()))


# Dynamic Programming
N = 0
dp = None
board = None


def findSticker():
    global dp
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    dp[0][1] = dp[1][0] + board[0][1]
    dp[1][1] = dp[0][0] + board[1][1]

    for i in range(2, N):
        dp[0][i] = max(dp[0][i - 2], dp[1][i - 2])
        dp[0][i] = max(dp[1][i - 1], dp[0][i])
        dp[0][i] += board[0][i]

        dp[1][i] = max(dp[0][i - 2], dp[1][i - 2])
        dp[1][i] = max(dp[0][i - 1], dp[1][i])
        dp[1][i] += board[1][i]


def main():
    global N, board, dp

    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        board = [[int(num) for num in input().split()] for _ in range(2)]
        dp = [[0] * 100001 for _ in range(2)]

        findSticker()

        print("#%d %d" % (test_case, max(dp[0][N - 1], dp[1][N - 1])))


# Permutation & Combination
combinationStack = []


def printString(cArr):
    for i in cArr:
        print(i, end='')
    print()


def swap(cArr, x, y):
    cArr[x], cArr[y] = cArr[y], cArr[x]


def permutation(cArr, l, r):
    if l == r:
        printString(cArr)
    else:
        for i in range(l, r + 1, 1):
            swap(cArr, l, i)
            permutation(cArr, l + 1, r)
            swap(cArr, l, i)


def push(ch):
    combinationStack.append(ch)


def pop():
    combinationStack.pop()


def combination(cArr, length, offset, k):
    if k == 0:
        printString(combinationStack)
    else:
        for i in range(offset, length - k + 1, 1):
            push(cArr[i])
            combination(cArr, length, i + 1, k - 1)
            pop()


def main():
    global cArr, N, K
    T = int(input())

    for test_case in range(1, T + 1):
        cArr = list(input())

        N = int(input())
        K = int(input())

        print("#%d" % test_case)

        permutation(cArr[0:N], 0, N - 1)
        combination(cArr, N, 0, K)


# DFS Algorithm
def depthFirstSearch(v, depth):
    global maxEdge

    if v == end:
        if maxEdge < 0 or depth < maxEdge:
            maxEdge = depth
        return

    visit[v] = True

    for i in range(1, vertex + 1):
        if MAP[v][i] == 1 and visit[i] is False:
            depthFirstSearch(i, depth + 1)
            visit[i] = False


def main():
    global vertex, end, visit, MAP, maxEdge

    T = int(input())

    for test_case in range(1, T + 1):
        vertex, edge, start, end = map(int, input().split())
        MAP = [[0] * (vertex + 1) for _ in range(vertex + 1)]
        visit = [False] * (vertex + 1)
        for _ in range(edge):
            v1, v2 = map(int, input().split())
            MAP[v1][v2] = 1
        maxEdge = -1
        depthFirstSearch(start, 0)
        print("#%d %d" % (test_case, maxEdge))


# BFS Algorithm
class Queue:
    class Point:
        def __init__(self, y, x, c):
            self.y = y
            self.x = x
            self.c = c

    def __init__(self, capacity):
        self.queue = [0] * capacity
        self.head = self.rear = 0

    def isEmpty(self):
        return self.head <= self.rear

    def enQueue(self, y, x, c):
        self.queue[self.head] = self.Point(y, x, c)
        self.head = self.head + 1

    def deQueue(self):
        if self.isEmpty():
            return None
        self.rear = self.rear + 1
        return self.queue[self.rear - 1]


def breadthFirstSearch():
    queue = Queue(row * column)
    queue.enQueue(0, 0, 0)
    MAP[0][0] = 0

    while queue.isEmpty() == False:
        p = queue.deQueue()

        if p.y == row - 1 and p.x == column - 1:
            return p.c

        if p.y + 1 < row and MAP[p.y + 1][p.x]:
            queue.enQueue(p.y + 1, p.x, p.c + 1)
            MAP[p.y + 1][p.x] = 0
        if p.x + 1 < column and MAP[p.y][p.x + 1]:
            queue.enQueue(p.y, p.x + 1, p.c + 1)
            MAP[p.y][p.x + 1] = 0
        if p.y - 1 >= 0 and MAP[p.y - 1][p.x] != 0:
            queue.enQueue(p.y - 1, p.x, p.c + 1)
            MAP[p.y - 1][p.x] = 0
        if p.x - 1 > 0 and MAP[p.y][p.x - 1] != 0:
            queue.enQueue(p.y, p.x - 1, p.c + 1)
            MAP[p.y][p.x - 1] = 0

    return -1


def main():
    global MAP, row, column
    T = int(input())

    for test_case in range(1, T + 1):
        row, column = map(int, input().split())
        MAP = [[int(num) for num in input().split()] for _ in range(row)]
        print("#%d %d" % (test_case, breadthFirstSearch()))


# Stack
stack = []


def stackInit():
    global stack
    stack.clear()


def stackIsEmpty():
    global stack
    return len(stack) == 0


def stackPush(value):
    stack.append(value)


def stackPop():
    return stack.pop()


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        stackInit()

        l = list(input().split())

        for i in l:
            stackPush(i)

        print("#%d" % test_case, end=' ')

        while not stackIsEmpty():
            value = stackPop()
            if value != None:
                print(value, end=' ')

        print()


# Queue
queue = []


def queueInit():
    global queue
    queue.clear()


def queueIsEmpty():
    global queue
    return len(queue) == 0


def queueEnqueue(value):
    queue.append(value)


def queueDequeue():
    return queue.pop(0)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        queueInit()
        l = list(input().split())

        for i in l:
            queueEnqueue(i)

        print("#%d" % test_case, end=' ')

        while not queueIsEmpty():
            value = queueDequeue()
            if value != None:
                print(value, end=' ')

        print()


# Hash
hash = {}


def find(key):
    return hash.get(key)


def add(key, value):
    hash.update({key: value})


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        for i in range(N):
            key, value = map(str, input().split())
            add(key, value)

        print("#%d" % test_case)

        Q = int(input())

        for i in range(Q):
            key = input()
            key = key.strip(" ")
            value = find(key)
            if value:
                print(value)
            else:
                print("not find")


# Tree
class Tree:
    MAX_CHILD_NUM = 2

    class TreeNode:
        def __init__(self, parent):
            self.parent = parent
            self.child = [-1] * Tree.MAX_CHILD_NUM

    def __init__(self, nodeNum):
        self.nodeNum = nodeNum
        self.treenode = [0] * (nodeNum + 1)

        for i in range(1, nodeNum + 1):
            self.treenode[i] = self.TreeNode(-1)

    def addChild(self, parent, child):
        found = -1

        for i in range(0, self.MAX_CHILD_NUM):
            if self.treenode[parent].child[i] == -1:
                found = i
                break

        if found == -1:
            return

        self.treenode[parent].child[found] = child
        self.treenode[child].parent = parent

    def getRoot(self):
        for i in range(1, self.nodeNum):
            if self.treenode[i].parent == -1:
                return i

        return -1

    def preOrder(self, root):

        print(root, end=' ')

        for i in range(0, self.MAX_CHILD_NUM):
            child = self.treenode[root].child[i]
            if child != -1:
                self.preOrder(child)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        node, edge = map(int, input().split())

        tree = Tree(node)

        numbers = [int(num) for num in input().split()]

        for i in range(0, edge * 2, 2):
            parent = numbers[i]
            child = numbers[i + 1]
            tree.addChild(parent, child)

        root = tree.getRoot()
        print("#%d" % test_case, end=' ')
        tree.preOrder(root)
        print()


# Graph
num_vertices = 0
adjListArr = list()


def createGraph(n):
    global adjListArr
    global num_verticess
    adjListArr = list()
    for i in range(n):
        adjListArr.append(list())
    num_vertices = n


def addEdge(src, dest):
    global adjListArr
    adjListArr[src].append(dest)
    adjListArr[dest].append(src)


def displayGraph(i):
    global adjListArr
    adjList = list(adjListArr[i])
    for i in adjList:
        print(i, end=' ')
    print()


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        V, E, Q = map(int, input().split())
        createGraph(V)

        for i in range(E):
            sv, ev = map(int, input().split())
            addEdge(sv, ev)

        print("#%d" % test_case)

        for i in range(Q):
            sv = int(input())
            displayGraph(sv)


# Linked List
class ListNode:
    data = 0
    prev = None
    next = None

    def __init__(self):
        self.data = 0
        self.prev = self
        self.next = self

    def appendListNode(head, data):
        node = ListNode()
        node.data = data
        if head == None:
            head = node
        else:
            last = head.prev
            last.next = node
            head.prev = node
            node.prev = last
            node.next = head
        return head

    def removeListNode(head, node):
        if head == head.next:
            return None
        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            if head == node:
                return nextNode
            else:
                return head


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        data = list(map(int, input().split()))

        head = None

        for i in range(N):
            head = ListNode.appendListNode(head, data[i])

        node = head

        while head != head.next:
            nextNode = node.next

            head = ListNode.removeListNode(head, node)
            node = nextNode.next.next

        print("#%d %d" % (test_case, head.data))
