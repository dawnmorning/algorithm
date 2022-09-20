# def subsetSum(i, N):
#     global result
#     if i == N:
#         temp = 0
#         for i in range(N+1):
#             if bit[i]:
#                 temp += A[i]
#
#         if temp == 0:      # 합이 10이면 개수 추가
#             result += 1
#             for i in range(N+1):
#                 if bit[i]:
#                     print(A[i], end=' ')
#             print()
#     else:
#         bit[i] = 1          # A[i]가 부분집합에 포함된 경우
#         subsetSum(i+1, N)
#         bit[i] = 0          # A[i]가 부분집합에 포함되지 않은 경우
#         subsetSum(i+1, N)
#
# n, s = map(int, input().split())
# A = list(map(int, input().split()))
# bit = [0]*(n+1)
# result = 0
#
# subsetSum(min(A), max(A))
# print(result)

import sys
from itertools import combinations
input = sys.stdin.readline
N, S = list(map(int, input().split()))
nums = list(map(int, input().split()))
cnt = 0
for i in range(1, len(nums)+1):
    result = combinations(nums, i)
    for num in result:
        if (sum(num) == S):
            cnt += 1
print(cnt)