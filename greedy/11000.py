import sys, heapq
sys.stdin = open('11000.txt')
input = sys.stdin.readline
n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()
time = sorted(time , key = lambda x:x[1])
possible = []
heapq.heappush(possible, time[0][1])
for i in range(1,n):
    if time[i][0] < possible[0]:
        heapq.heappush(possible, time[i][1])
    else:
        heapq.heappop(possible)
        heapq.heappush(possible, time[i][1])
print(len(possible))



