# kruskal
import sys

sys.stdin = open('1197.txt')


def findset(rep_list,x):
    while rep_list[x] != x:
        x = rep_list[x]
    return x

def union(rep_list, a ,b):
    a = findset(rep_list,a)
    b = findset(rep_list,b)
    if a<b:
        rep_list[b] = a
    else:
        rep_list[a] = b

V,E = map(int, input().split())
rep_list = [i for i in range(V+1)]
edges = []
result = 0
for _ in range(E):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key = lambda x : x[2])
for edge in edges :
    a,b,cost = edge
    if findset(rep_list, a) != findset(rep_list,b):
        union(rep_list,a,b)
        result += cost
print(result)

'''
1. 아이디어
- MST기본문제, 외우기
- 간선을 인접리스트에 넣기
- 힙에 시작점 넣기
- 힙이 빌때까지 다음의 작업을 반복
    - 힙의 최소값 꺼내서, 해당 노드 방문 안 했다면
        - 방문 표시, 해당 비용추가, 연결된 간선들 힙에 넣어주기

2. 시간 복잡도
- MST : O(ElogE)

3. 자료궂
- 간선 저장 되는 인접리스트 : (무게, 노드번호)
- 힙: (무게, 노드번호)
- 방문 여부 : bool[]
- MST결과값 : int
'''
import sys
input = sys.stdin.readline
sys.stdin = open('1197.txt')
import heapq
v, e = map(int, input().split())
edge = [[] for _ in range(v+1)]
check = [False] * (v+1)
res = 0
for i in range(e):
    a,b,c = map(int, input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])
heap = [[0,1]]
while heap :
    w, each_node = heapq.heappop(heap)
    if check[each_node] == False:
        check[each_node] = True
        res += w
        for next_edge in edge[each_node]:
            if check[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)
print(res)