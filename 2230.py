import sys
input = sys.stdin.readline

n,m = map(int, input().split())
list = []
for _ in range(n):
    a = int(input())
    list.append(a)
list.sort()
res = 9876543210
start = 0
end = 0
while start < n:
    sub = abs(list[start] - list[end])
    if sub >= m :
        res = min(res, sub)
        if sub == m:
            break
        start += 1
        end = start
        continue

    end += 1
    if end == n:
        start += 1
        end = start
print(res)