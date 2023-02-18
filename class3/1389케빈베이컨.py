# import sys
# input = sys.stdin.readline
# from collections import deque

# def bfs(v):
#     q = deque([v])
#     visited[v] = 1
#     while q : 
#         next_room = q.popleft()
#         # 친구이고 탐색하지 않았다면 들어가기
#         for i in information[next_room]:
#             if not visited[i]:
#                 visited[i] = visited[next_room] +1
#                 q.append(i)

# n, m = map(int, input().split())
# information = [[] for _ in range(n+1)]
# for i in range(m):
#     a,b  = map(int, input().split())
#     # 양방향이기 때문
#     information[a].append(b)
#     information[b].append(a)
# answer = []

# # 1번부터 n번명까지 돌아야하므로
# for j in range(1, n+1):
#     visited = [0] * (n+1)
#     bfs(j)
#     answer.append(sum(visited))
# print(answer.index(min(answer))+1)

import sys
input = sys.stdin.readline
inf = int(1e9)
n,m = map(int, input().split())
graph = [[inf] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b]= 1
    graph[b][a] = 1

# 나에게서 나한테로는 0
for i in range(1, n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] =0

# k는 거쳐가는 지점
# N^3 ???????           
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            # 중간 거쳐서 가는 방법과 직접 가는 방법 중 최솟 값
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

minV = inf
for i in range(n):
    answer = 0
    for j in range(n):
        answer = graph[i][j]
    if minV > answer : 
        answer = minV
        idx = i
print(idx + 1)


