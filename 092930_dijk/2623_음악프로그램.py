import sys
sys.stdin = open('2623.txt')
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
singer = [ [] for _ in range(n+1)]
indegree = [0] * (n+1)

# 간선 정보
for _ in range(m):
    num = list(map(int, input().split()))
    for i in range(1, num[0]):
        singer[num[i]].append(num[i+1])
        indegree[num[i+1]] += 1

q = deque()
res = []
for j in range(1,n+1):
    if indegree[j] == 0:
        q.append(j)
        res.append(j)

while q:
    temp = q.popleft()
    for k in singer[temp]:
        indegree[k] -= 1
        if indegree[k] == 0:
            q.append(k)
            res.append(k)

if len(res) != n:
    print(0)
else:
    for l in res:
        print(l)

