import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    count, s = input().split()
    count = int(count)
    answer = ''
    for i in s:
        answer += count * i
    print(answer)