from collections import deque
def dfs(v):
    visited1[v] = 1
    print(v, end= ' ')
    for w in adjlist[v]:
        if not visited1[w]:
            dfs(w)

def bfs(v):
    q = deque()
    q.append(v)
    print(v, end = ' ')
    visited2[v] = 1
    while q:
        tmp = q.popleft()
        for w in adjlist[tmp]:
            if visited2[w] == 0:
                q.append(w)
                visited2[w] = 1
                print(w, end= ' ')

n, m, v = map(int, input().split())
adjlist = [[] for _ in range(n+1)]
visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)
for _ in range(m):
    a, b = map(int,input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
for i in range(n+1):
    adjlist[i].sort()
dfs(v)
print()
bfs(v)