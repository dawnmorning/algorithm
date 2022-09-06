import sys
from collections import deque
sys.stdin = open('10026.txt')
input = sys.stdin.readline
n = int(input())
test = [list(map(str, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
q = deque()
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):
    q.append([r,c])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and test[nr][nc] == test[r][c]:
                q.append([nr,nc])
                visited[nr][nc] = 1
# 색약 X
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1
print(cnt, end  = ' ')

# 색약 o
cnt1 = 0
for i in range(n):
    for j in range(n):
        if test[i][j] == 'R':
            test[i][j] == 'G'
visited = [[0] * n for _ in range(n)]


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1
print(cnt1)


