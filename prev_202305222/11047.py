import sys
sys.stdin = open('11047.txt')
n,k = map(int, input().split())
li = []
for _ in range(n):
    a = int(input())
    li.append(a)


cnt = 0
for i in range(len(li)-1,-1,-1):
    if li[i] <= k:
        cnt += (k // li[i])
        k -= (li[i] * (k // li[i]))
print(cnt)