import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    value = input().split()
    if value[0] == "push":
        stack.append(int(value[1]))
        # print(stack)
    elif value[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif value[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif value[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif value[0] == "size":
        print(len(stack))