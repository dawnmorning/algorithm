import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    i = int(input())
    li.append(i)
li.sort()
for j in li:
    print(j)
