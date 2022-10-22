import sys
input = sys.stdin.readline
n = int(input())
tester = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0
for i in range(n):
    flag = False
    while tester[i] != 0:
        if flag == False:
            tester[i] = tester[i] - b
            cnt += 1
            flag = True
        if tester[i] >= c:
            tester[i] = tester[i] - c
            cnt += 1
        if tester[i] == 0:
            break
        elif tester[i] < c:
            cnt += 1
            tester[i] = 0
            break


print(cnt)
