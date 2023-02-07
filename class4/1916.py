import heapq, sys
input = sys.stdin.readline



n = int(input())
m = int(input())
data = [[] for _ in range(n+1)]
distance = [987654321] * (n+1)

for _ in range(m):
    i, j, fear = map(int, input().split())
    data[i].append((j,fear))
start, end = map(int, input().split())


def dijkstra(start):
    q= []
    heapq.heappush(q, (start,0))
    distance[start] = 0
    while q:
        current_position, temp = heapq.heappop(q)
        if distance[current_position] < temp:
            continue
        for next_position, value in data[current_position]:
            cost = temp + value
            if cost < distance[next_position]:
                distance[next_position] = cost
                heapq.heappush(q,(next_position, cost))


dijkstra(start)
print(distance[end])

