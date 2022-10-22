from collections import deque

def bfs(r,c):
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr,nc))
    return arr[n-1][m-1]

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dr = [0,0,-1,1]
dc = [1,-1,0,0]
start,end = 0,0
x = bfs(start,end)
print(x)
