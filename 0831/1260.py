import sys
from collections import deque
sys.stdin = open('1260.txt')
input = sys.stdin.readline
n,m,v = map(int, input().split())
visited = [0] * (n+1)
adjlist = [[]for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

def dfs(adjlist, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in sorted(adjlist[v]):
        if not visited[i]:
            dfs(adjlist, i, visited)

def bfs(adjlist, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in sorted(adjlist[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                bfs(adjlist, i, visited)

dfs(adjlist,v,visited.copy())
print()
bfs(adjlist,v,visited.copy())



