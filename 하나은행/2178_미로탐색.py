import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj, ei ,ej):
    q = deque()
    v = [[0] * m for _ in range(n)]
    q.append((si,sj))
    v[si][sj] = 1
    while q:
        ti, tj = q.popleft()
        if (ti, tj) == (ei, ej):
            return v[ei][ej]
        di, dj = [1-1,0,0], [0,0,1,-1]
        for k in range(4):
            ni, nj = ti + di[k], tj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = 1 

n,m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n) ]
answer = bfs(0,0,n-1,m-1)
print(answer)

