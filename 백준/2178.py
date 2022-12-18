import sys
input = sys.stdin.readline

def bfs(sj,si, ei, ej):
    q = []
    v = [[0] * m for _ in range(n)]
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (ei,ej):
            return v[ei][ej]

        di ,dj = [1,-1,0,0], [0,0,-1,1]
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
n, m = map(int, input().split())
maze = [list(map(int, input().rstrip()))for _ in range(n)]
ans = bfs(0,0, n-1, m-1)
print(ans)