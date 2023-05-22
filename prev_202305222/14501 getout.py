import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
for _ in range(n):
    t, p = list(map(int, input().split()))
    


        #현재 일에 뒤에 일수 더한 일당과
        #뒷날에 뒷날 일수 더한 일당 비교해서 어디가 더 나은가? 재귀,,,