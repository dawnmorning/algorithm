from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
deq = deque()
for i in range(n):
    word = input().split()
    if word[0] == "push":
        deq.append(word[1])
    elif word[0] == "pop":
        if not deq :
            print("-1")
        else: 
            deq.pop(0)
    elif word[0] == "size":
        print(len(deq))
    elif word[0] == "empty":
        if not deq :  # if len(deq) == 0           
            print("1")
        else:
            print("0")
    elif word[0] == "front":
        if not deq:
            print("-1")
        else:
            print(deq[0])
    elif word[0] == "back":
        if not deq:
            print("-1")
        else:
            print(deq[-1])

