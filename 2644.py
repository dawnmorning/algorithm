import sys
from collections import deque
input = sys.stdin.readline

def bfs(s, e):
    q = deque()
    q.append(s)
    while q:
        vs = q.popleft()
        for v in link[vs]:
            if visit[v] == -1:
                visit[v] = visit[vs] + 1
                if v == e:
                    return visit[v]
                q.append(v)
    return -1

n = int(input())
s, e = map(int, input().split())
m = int(input())
link = [[] for _ in range(n + 1)]
visit = [-1] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

visit[s] = 0
print(bfs(s, e))