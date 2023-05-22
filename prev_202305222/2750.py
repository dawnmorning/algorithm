import sys
n_list= []
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    n_list.append(num)
    s = sorted(n_list)
for j in s:
    print(j)
