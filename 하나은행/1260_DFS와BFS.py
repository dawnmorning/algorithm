import sys
input = sys.stdin.readline

def dfs(graph, v):
    global n, m
    
    print(v,end = ' ')
    visited[v] = 1
    for i in graph[v]:
        if visited[i]==0:
            visited[i] == 1
            dfs(graph,i)

def bfs(graph,v):
    q = []
    q.append(v)
    visited_2[v] = 1
    while q:
        j = q.pop(0)
        print(j, end= ' ')
        for k in graph[j]:
            if not visited_2[k]:
                q.append(k)
                visited_2[k] = 1


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[0] * (n+1)
visited_2 = [0] * (n+1)
dfs(graph,v)
print()
bfs(graph,v)