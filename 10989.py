import sys
input = sys.stdin.readline
n = int(input())
pod = [0] *10001
for i in range(n):
    pod[int(input())] += 1
for i in range(10001):
    if pod[i] !=0:
        for k in range(pod[i]):
            print(i)