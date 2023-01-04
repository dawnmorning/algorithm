import sys
input = sys.stdin.readline
n = int(input())
stair = [0] * 301
for _ in range(n):
    stair[_] = int(input())
dp = [0] * 301
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1]+ stair[2])
for i in range(3,n):
    dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    # 네번째 계단 -> (1번째까지 최대 + 3번째 + 네번째 or 2번째까지 젤 큰거 + 나) 
print(dp[n-1])