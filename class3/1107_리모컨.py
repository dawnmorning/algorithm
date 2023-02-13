import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
a = [True for _ in range(10)]

if m != 0:
    abnormal = list(map(int, input().split()))
    for i in abnormal:
        a[i] = False

cnt = abs(n - 100)
for i in range(1000001):
    list_i = list(str(i))
    flag = 0
    for c in list_i:
        if a[int(c)] == 1:
            continue
        else:
            flag = 1
            break

    if flag:
        continue
    else:
        # 무지성 + or - , + or - 를 눌러야할 횟수 + 누른 버튼 숫자 길이
        cnt = min(cnt, abs(n - i) + len(list_i))

print(cnt)