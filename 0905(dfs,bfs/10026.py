import sys
sys.stdin = open('10026.txt')
input = sys.stdin.readline
n = int(input())
test = [list(map(str, input().rstrip())) for _ in range(n)]

print(test)