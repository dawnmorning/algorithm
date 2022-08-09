import sys
input = sys.stdin.readline
k = int(input())
li = []
total = 0
for i in range(k):
    shout = int(input())
    if shout:
        li.append(shout)
    else:
        li.pop()
for j in li:
    total += j
print(total)
