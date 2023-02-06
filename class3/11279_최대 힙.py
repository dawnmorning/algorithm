import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    a= int(input())
    if a == 0:
        if heap:
            print((-1) * heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, (-1)*a)

# heappop() 함수, heappush() 함수는 최소힙만 동작하기 때문에 최대힙을 구현하기 위해서는 약간의 변형이 필요하다.

# 넣어주는 값에 -1을 곱해 heap에 push를 해주면 가장 큰 값이 음수가 되면 가장 작은 값이 되기 때문에 최대힙 구현이 가능하다. 
# heap에서 pop을 해줄 때만 -1을 다시 곱해주면 원래 숫자를 출력할 수 있다. 