'''
한 점에서 다른 모든 점으로의 최단경로 -> 다익스트라
모든 점 거리 초기값 무한대로 설정
시작점 거리0 설정, 힙에 추가
힙에서 빼면서 다음 것들 수행
    - 최신 값인지 확인
    - 간선을 타고 간 비용이 더 작으면 갱신


2. 시간복잡도
- 다익스트라 : O(ElogN)
    - E : 3e5
    - V:  2e4, logv  ~= 20
    - ElpV = 6e6 > 가능

3. 변수

= 힙 : (비용, 노드번호)
- 거리 배열 : 비용 : int[]
- 간선저장, 인접리스트 = (비용,노드번호)

'''



import sys
input = sys.stdin.readline
import heapq
v,e = map(int, input().split())
inf = 100000000
adjlist = [ [] for _ in range(v+1)]

dist = [inf] * (v+1)
n = int(input())

for i in range(e):
    u,v,w = map(int, input().split())
    adjlist[u].append([w,v])

dist[n] = 0
heap= [[0,n]]

while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in adjlist[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew+nw
            heapq.heappush(heap, [dist[nv], nv])
for i in range(1,len(dist)):
    if dist[i] == inf :
        print('INF')
    else:
        print(dist[i])


import sys
import heapq
v, e = map(int, input().split())
n = int(input())
inf = 10000000000
adjlist = [[] for _ in range(v+1)]
cost = [inf] * (v+1)
n = int(input())
for i in range(e):
    s,e,w = map(int, input().split())
    adjlist[s].append([e,w])

cost[n] = 0
heap= [[0,n]]
while heap:
    ew, ev = heapq.heappop(heap)
    if cost[ev] != ew:
        continue
    for next_cost, next_end in adjlist[ev]:
        if cost[next_end] > ew + next_cost:
            cost[next_end] = ew + next_cost
            heapq.heappush(heap,[cost[next_end], next_end])
for i in range(1, len(len(cost))):
    if cost[i] == inf:
        print('INF')
    else:
        print(i)

