import sys
input = sys.stdin.readline
n, m = map(int, input().split())
S = []
M = []
for i in range(n):
  s = input().strip()
  S.append(s)
# print(S)
cnt = 0
for j in range(m):
    m = input().strip()
    if m in S:
        cnt+=1
print(cnt)
# print(M)