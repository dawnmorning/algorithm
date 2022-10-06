import heapq
import sys
input = sys.stdin.readline

n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
inf = 10000 ** 3
for _ in range(m):
    n1,n2,cost = map(int, input().split())
    graph[n1].append((n2,cost))

def dijkstra(s):
    q = []
    d = [inf] * (n+1)
    heapq.heappush(q, (0,s))
    d[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue
        for next_i, next_cost in graph[now]:
            cost = dist + next_cost
            if d[next_i] > cost:
                d[next_i] = cost
                heapq.heappush(q,(cost, next_i))
    return d

res = 0
for i in range(1, n+1):
    start = dijkstra(i)
    ret = dijkstra(x)
    res = max(res, start[x] + ret[i])  # x까지 가는데 최단거리 + i로 오는데 최단거리 중 최대값
print(res)