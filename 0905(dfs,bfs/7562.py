from collections import deque
import sys
sys.stdin = open('7562.txt')
# input = sys.stdin.readline
t = int(input())
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]
for _ in range(t):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    q = deque()
    now_x,now_y = map(int,input().split())
    ob_x, ob_y = map(int, input().split())
    q.append((now_x, now_y))
    while q:
        x,y = q.popleft()
        if x == ob_x and y == ob_y:
            break
        for i in range(8):
            nx = x + dr[i]
            ny = y + dc[i]
            if nx<0 or ny<0 or nx >= l or ny >=l:
                continue
            if chess[nx][ny] == 0 :
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx,ny))
    print(chess[ob_x][ob_y])
