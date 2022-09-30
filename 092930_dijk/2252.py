import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
tall = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    tall[a].append(b)
    visited[b] += 1  # 차수

q = deque([])
for i in range(1, n+1):
    if visited[i] == 0:   # 차수가 0이면 추가
        q.append(i)

res = []
while q:
    now = q.popleft()
    res.append(now)
    for next in tall[now]:
        visited[next] -= 1
        if visited[next] == 0: # 차수가 0이면 q에 추가
            q.append(next)
print(*res)