import sys
from collections import deque
sys.stdin = open('2178.txt')
input = sys.stdin.readline
n, m = map(int, input().split())
road = [list(map(int, input().rstrip()))for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    que = deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and road[nx][ny] == 1:
                road[nx][ny] = road[x][y] + 1
                que.append((nx,ny))
    return road[n-1][m-1]
print(bfs(0,0))