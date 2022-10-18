from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for r in range(n):
    for c in range(n):
        if arr[r][c] == 9:
            sr,sc = r,c
            arr[r][c] = 0

size = 2
cnt = 0
eat = 0
def eat_fish(sr,sc):
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    global size
    visited = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    q = deque()
    q.append((sr,sc))
    visited[sr][sc] = 1
    temp = []
    while q:
        x,y = q.popleft()
        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0 <= nr < n and 0 <= nc < n :
                if arr[nr][nc] <= size and visited[nr][nc] == 0:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
                    dist[nr][nc] = dist[x][y] + 1
                    if arr[nr][nc] != 0 and arr[nr][nc] < size: # 물고기 먹을수 있고 가능하다면
                        temp.append((nr,nc,dist[nr][nc]))
    temp.sort(key = lambda x : (x[2],x[0],x[1]))  # 거리 낮은순, 가로 세로
    return temp
while True:
    li = eat_fish(sr, sc)
    if len(li) == 0:
        break
    sr,sc,dist = li[0]
    cnt += dist
    eat += 1
    arr[sr][sc] = 0
    if eat == size:
        size += 1
        eat = 0
print(cnt)





