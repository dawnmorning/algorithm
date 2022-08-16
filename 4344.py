import sys
input = sys.stdin.readline
c = int(input())
for tc in range(c):
    num = list(map(int,input().split()))
    total = 0
    for i in range(1, len(num)):
        total += num[i]
    a_ve = total / len(range(1,len(num)))
    count = 0
    for j in range(1,len(num)):
        if num[j] > a_ve:
            count += 1
    value = count / len(range(1,len(num)))
    r_value = round(value, 3)
    print(f'{r_value*100}%')
































































