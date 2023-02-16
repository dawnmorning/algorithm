import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for i in range(n):
    n = int(input())
    
    if n == 0:
        if len(arr):
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, n)