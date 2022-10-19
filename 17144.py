import sys
input = sys.stdin.readline
r,c,t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if arr[i][0] == -1:
        up = i
        donw = i +1
        break

def micro():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] == 0 or arr[x][y] == -1:
                continue

            microdust = arr[x][y] // 5

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                    visited[nx][ny] += microdust
                    visited[x][y] -= microdust
    for i in range(r):
        for j in range(c):
            arr[i][j] += visited[i][j]
