import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)
print(family)

def bfs(s):
    queue = deque([s])
    visited[s] = 1
    while queue:
        x = queue.popleft()
        for fam in family[x]:
            if fam == b:
                print(visited[x])
                break
            if not visited[fam]:
                visited[fam] = visited[fam] + 1
                queue.append(fam)
bfs(a)
print(-1)
