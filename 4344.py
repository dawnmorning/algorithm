import sys
input = sys.stdin.readline
c = int(input())
for tc in range(c):
    num = list(map(int,input().split()))
    total = 0
    for i in range(1, len(num)):
        total += num[i]
    a_ve = total / len(num)
    count  = 0
    for j in range(1,len(num)):
        if num[j] > a_ve:
            count += 1

    print(count / len(range(1, len(num))
































































