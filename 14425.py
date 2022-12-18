import sys
input = sys.stdin.readline
n, m = map(int, input().split())
S = []
for i in range(n):
  s = input()
  S.append(s)
# print(S)
cnt = 0
for j in range(m):
    m = input()
    if m in S:
        cnt+=1
print(cnt)
# print(M)