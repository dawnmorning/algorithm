# 문제
# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 
# 1번 집부터 한 줄에 하나씩 주어진다. 
# 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 3
# 26 40 83
# 49 60 57
# 13 89 99

# 1번 선택 -> 2 3번 중 값 작은 놈.
# 만약 3번 선택 -> 1, 2번 중 값 작은 놈.
# 앞번호와만 다르기만 하면 됨 (이전 집)
n = int(input())
house_info = []
for i in range(n):
    house_info.append(list(map(int, input().split())))
    # 첫 턴 각자에서 출발
for j in range(1,n):
    # 두번째 턴부터 
    house_info[j][0] = house_info[j][0] +  min(house_info[j-1][1], house_info[j-1][2]) # 2번째에서 R을 선택했다면, 1번째는 G or B
    house_info[j][1] = house_info[j][1] +  min(house_info[j-1][0], house_info[j-1][2]) # 2번째에서 G를 선택했다면, 1번째는 R or B
    house_info[j][2] = house_info[j][2] + min(house_info[j-1][0], house_info[j-1][1])  # 상동 논리
# print(house_info[n-1])
print(min(house_info[n-1]))