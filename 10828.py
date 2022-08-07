import sys

def push(x):
    stack.append(x)
def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()
def size():
    return len(stack)
def empty():
    return 0 if stack else 1
def top():
    if stack:
        return stack[-1]
    else:
        return -1
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    value = input().split()
    value_find = value[0][0]

    if value_find == "push":
        print(push(value[0][1]))
    elif value_find == "pop":
        print(pop())
    elif value_find == "size":
        print(size())
    elif value_find == "empty":
        print(value())
    elif value_find == "top":
        print(top())
