import sys
sys.stdin = open('1026.txt')
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
value = 0
for i in range(n):
    value += min(b) * max(a)
    a.remove(max(a))
    b.remove(min(b))
    # print(b)
print(value)