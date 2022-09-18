# from itertools import permutations
#
# n, m = map(int, input().split())
#
# for i in list(permutations(list(range(1, n+1)), m)):
#     print(' '.join(map(str, i)))

from collections import deque

n, m = map(int, input().split())
visited = [False] * n

q = deque()


def backtrack(k):
    if k == m:
        print(*q)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True

            q.append(i + 1)
            backtrack(k + 1)

            visited[i] = False
            q.pop()
backtrack(0)