import heapq, sys
input = sys.stdin.readline



n = int(input())
m = int(input())
data = [[] for _ in range(n+1)]
visited = [987654321] * (n+1)


# 각 시작점
for _ in range(m):
    i, j, fear = map(int, input().split())
    # data = [[]   [(2,2),(3,3)]   []] ...
    data[i].append((j,fear))
start, end = map(int, input().split())


def dijkstra(start):
    # [(n번으로 가는데, 얼마만큼 들었음)]
    q= []
    # q = []
    heapq.heappush(q, (start,0))
    visited[start] = 0
    # q가 빌 때까지 현재 위치와 그 위치의 값을 꺼내서 최단거리 비교
    while q:
        # [(2, 2), (3, 3), (4, 1), (5, 10)]
        current_position, temp = heapq.heappop(q)

        # 새로 뽑아낸 값이 현재 있는 곳의 값보다 크다면 패스
        if visited[current_position] < temp:
            continue

        # 저장되어 있는 최소 값보다 작으면 갱신하고 비교한 위치와 최소값을 q에 넣음 
        for next_position, value in data[current_position]:
            cost = temp + value
            if cost < visited[next_position]:
                visited[next_position] = cost
                heapq.heappush(q,(next_position, cost))

# 클래스 4 !
dijkstra(start)
print(visited[end])

