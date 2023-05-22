import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0, 0
temp = nums[0]
res = 100001
while True:
    if temp >= s:
       temp -= nums[start]
       res = min(res, end - start + 1)
       start += 1
    else:
        end += 1
        if end == n:
            break
        temp += nums[end]

if res == 100001:
    print(0)
else:
    print(res)
