import sys
input = sys.stdin.readline
n,m,v = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
    adj[s].sort()
    adj[e].sort()

def dfs(adj, v, visited):

    visited[v] = 1
    print(v, end=' ')
    for i in adj[v]:
        if not visited[i]:
            dfs(adj, i, visited)

def bfs(adj,v, visited):
    
    q = [v]
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v, end= ' ')
        for j in adj[v]:
            if not visited[j]:
                q.append(j)
                visited[j] = 1
dfs(adj, v, visited)
print("")
visited = [0] * (n+1)
bfs(adj, v, visited)