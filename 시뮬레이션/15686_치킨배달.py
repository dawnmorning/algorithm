import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
customer = []      # 집의 좌표
bbq = []      # 치킨집의 좌표

# 돌면서 담아준다
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            customer.append([i, j])
        elif city[i][j] == 2:
            bbq.append([i, j])
            
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때,
for chi in combinations(bbq, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in customer: 
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)