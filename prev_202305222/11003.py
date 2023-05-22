import sys
input = sys.stdin.readline

from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))
d = [0] * n
q = deque()
for i in range(n):
    # q의 마지막 보다 다음 들어올 값이 작은 경우에, 이전 값을 지워버리자
    while q and q[-1][1] > arr[i]:
        q.pop()

    # 범위 안의 인덱스를 벗어날 경우 날림
    while q and q[0][0] <= i-l:
        q.popleft()
    q.append((i, arr[i]))
    d[i] = q[0][1]
print(*d)
