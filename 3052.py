import sys
input = sys.stdin.readline
check = [0] * 42
for i in range(10):
    a = int(input())
    b = a % 42
    if check[b] == 0 :
        check[b] = 1
    else:
        continue
print(check.count(1)) 