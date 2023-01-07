from sys import stdin
import heapq

heap = []

for _ in range(int(input())):
    x = int(stdin.readline())

    if x == 0:
        if heap:
            val, sgn = heapq.heappop(heap)
            print(val * sgn)
        else:
            print(0)
    # 힙에 [절댓값, 부호]를 넣어두고 heappop해서 사용하면 갓-파이썬은 comparator 같은 거 사용하지 않아도

    # 1. 절댓값이 작은 수
    # 2. 절댓값이 같으면 부호가 음인 수
    else:
        heapq.heappush(heap, [abs(x), x//abs(x)])