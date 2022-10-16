from collections import deque

chain = []
for _ in range(4):
    chain.append(deque((map(int, list(input())))))
n = int(input())
for _ in range(n):
    idx, direct = map(int, input().split())

    rotation = [0] * 4
    rotation[idx-1] = direct

    for i in range(idx,4):
        if chain[i-1][2] != chain[i][6]:
            rotation[i] = -rotation[i-1]
    for i in range(idx-2,-1,-1):
        if chain[i+1][6] != chain[i][2]:
            rotation[i] = -rotation[i+1]

    for i in range(4):
        chain[i].rotate(rotation[i])

res = 0
for i in range(4):
    res += chain[i][0] * 2 ** i
print(res)