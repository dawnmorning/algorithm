import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
adjlist = [[] for _ in range(n+1)]
for _ in range(m):
    a, b= map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
visit = [0] * (n+1)

def dfs(adjlist, v, visited):
    visit[v] = 1
    for i in adjlist[v]:
        if visit[i] == 0:
            dfs(adjlist, i , visited)

dfs(adjlist, 1, visit)
print(visit.count(1) - 1)