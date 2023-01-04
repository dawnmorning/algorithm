# 가로칸의 수 m: 열 , n:행 , 상자의 수 : h
# 1: 익음, 0: 익지 않음, -1 :들어있지 않음
import sys
from collections import deque
input = sys.stdin.readline
m,n,h = map(int, input().split())

dr = [-1,1,0,0,0,0]
dc = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

box = [[list(map(int, input().split()))for _ in range(n)] for _ in range(h)]
q = deque()

# 익은 토마토들 하나씩 큐에 넣기
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                # 높이/행/열/일 수
                q.append((i,j,k,0))
while q:
    height, r,c, day = q.popleft()
    # 방향 돌기
    for i in range(6):
        nh = height + dz[i]
        nr = r + dr[i]
        nc = c + dc[i]
        temp_day = day + 1

        # 범위 안에 있고 익을 수 있으면
        if 0 <= nr < n and 0 <= nc < m and 0 <= nh < h:
            if box[nh][nr][nc] == 0:
                # 익게 하고 위치 넣어 q에 주기
                box[nh][nr][nc] = 1
                q.append((nh,nr,nc,temp_day))

# 익게 했는데, 주위에 친구가 없어서 0인 토마토가 있을 경우 day는 될 수 없으므로 값을 -1로 주고 break
for i in range(h):
    for j in range(n):
        if box[i][j].count(0) > 0 :
            day = -1
            break
# print(box[1][1])
# print(box)
print(day)