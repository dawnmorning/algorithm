import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
v = int(input())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer= 0 
for _ in range(v):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
q=deque()
q.append(1)
while q:
    u = q.popleft()
    visited[u] = 1
    for i in adj[u]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)
            answer += 1
print(answer)


