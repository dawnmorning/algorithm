# O(2^N)
# 어떤 문제가 그리디로 풀린다면, 이 문제는 DP로도 가능
# 데이터의 크기가 말도 안 된다면, 그 다음에 그리디를 생각하는게 낫다.
# N -> 1,500,000
# dp[N] -> dp[i] : i번째 일부터 상담을 받을 때, 벌 수 있는 최대금액
# 일을 한다 / 안 한다
# price[i] + date[i]
# dp[i] = max(price[i] + dp[i+date[i],dp[i+1]])

# import sys
# def input():
#     return sys.stdin.readline().rstrip()

# n = int(input())
# t, p = [], []
# dp = [-1 for i in range(n+1)]

# for i in range(n):
#     a, b= map(int, input().split())
#     t.append(a)
#     p.append(b)

# def call_dp(num):
#     if num == n:
#         return 0
#     # 반환할 때 헷갈리지 말자
#     # 경우의수 -> 1반환해야 (끝까지 왔다, 만족하는 경우의 수 하나 찾았다.)
#     # 합 -> 0반환해야 (끝까지 왔다, 더 더할 숫자가 없다.)
#     if dp[i] != -1:
#         return dp[i]
#     dp[i] = dp[i+1]
    
#     if num + t[num] > n:
#         dp[i] = max(dp[i],p[i]+dp[i+t[i]])
#     return dp[i]



import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
t, p = [], []
dp = [-1 for i in range(n+1)]

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n):
    if t[i] + i <= n:
        dp[i+t[i]] = max(dp[i+t[i]],dp[i]+p[i])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[-1]+1)

