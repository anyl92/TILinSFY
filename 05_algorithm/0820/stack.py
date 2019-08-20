data = ['A', 'B', 'C']
stack = []

def push(data):
    for i in data:
        stack.append(i)
    return stack

def pop(stack):
    if len(stack) == 0:
        return
    return stack.pop()

def feek(stack):
    if len(stack) == 0:
        return
    return stack[-1]
print(push(data), feek(stack), pop(stack), pop(stack), pop(stack), pop(stack))