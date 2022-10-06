import sys
input = sys.stdin.readline

def findset(x):
    while x != rep_list[x]:
        x = rep_list[x]
    return rep_list[x]

def union(x,y):
    rep_list[findset(y)] = findset(x)

    if x < y :
        rep_list[y] = x
    else:
        rep_list[x] = y


n = int(input())
graph = [list(map(int, input().split()))for _ in range(n)]
rep_list = [i for i in range(n)]

edges = []
for i in range(n):
    for j in range(i+1,n):
        edges.append([graph[i][j],i,j])
edges.sort()
cost = 0

for w,n1,n2 in edges:
    if findset(n1) != findset(n2):
        union(n1,n2)
        cost += w
print(cost)

