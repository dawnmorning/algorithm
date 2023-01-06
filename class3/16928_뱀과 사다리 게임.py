from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0]*101
visit = [0]*101
lad = [0]*101
sna = [0]*101
for _ in range(n):
    x, y = map(int, input().split())
    lad[x]=y
for _ in range(m):
    u, v = map(int, input().split())
    sna[u]=v
q = deque()
def bfs(x):
    q.append(x)
    visit[x]=1
    while q:
        x = q.popleft()
        for i in range(1, 7):
            nx = x + i
            if 0<nx<=100 and visit[nx]==0:
                if lad[nx]!=0:
                    nx = lad[nx]
                elif sna[nx]!=0:
                    nx = sna[nx]
                if visit[nx]==0:
                    q.append(nx)
                    visit[nx]=1
                    arr[nx]=arr[x]+1
bfs(1)
print(arr[100])
