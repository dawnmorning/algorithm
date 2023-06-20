import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    value = input().split()
    if value[0] == "push":
        li.append(value[1])
    elif value[0] == "pop":
        if li: print(li.pop())
        else: print(-1)
    elif value[0] == "size":
        print(len(li))
    elif value[0] == "empty":
        if len(li) == 0: print(1)
        else: print(0)
    elif value[0] == "front":
        if len(li) == 0: print(-1)
        else: print(li[0])
    elif value[0] == "back":
        if len(li) == 0: print(-1)
        else: print(li[-1])
# from sys import stdin

# N = int(stdin.readline())
# Que = []
# for i in range(N) :
#     A = stdin.readline().split()

#     if A[0] == 'push' : Que.append(A[1])

#     elif A[0] == 'pop' : 
#         if Que : print(Que.pop(0))
#         else : print(-1)

#     elif A[0] == 'size' : print(len(Que))

#     elif A[0] == 'empty' :
#         if len(Que) == 0 : print(1)
#         else : print(0)
            
#     elif A[0] == 'front' :
#         if len(Que) == 0 : print(-1)
#         else : print(Que[0])
    
#     elif A[0] == 'back' :
#         if len(Que) == 0 : print(-1)
#         else : print(Que[-1])