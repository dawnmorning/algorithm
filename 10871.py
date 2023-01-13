import sys
input = sys.stdin.readline
n, x = map(int, input().split())
arr = list(map(int, input().split()))
answer = []
for _ in arr:
    if x > _ :
        answer.append(_)
print(*answer)

