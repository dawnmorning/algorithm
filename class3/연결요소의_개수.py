import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(v):
    visited[v] = 1
    for j in adj[v]:
        if not visited[j]:
            dfs(j)


n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)