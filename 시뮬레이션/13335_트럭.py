# n은 다리를 건너는 트럭의 수, w는 다리의 길이, 그리고 L은 다리의 최대하중을 나타낸다.
# 4,2,10
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w  # 다리를 나타내는 리스트를 선언하고, 0으로 초기화
time = 0  # 경과 시간을 나타내는 변수
total_weight = 0  # 다리 위의 트럭들의 무게 합을 나타내는 변수

while bridge:
    time += 1  # 1초가 경과함
    total_weight -= bridge.pop(0)  # 다리의 가장 왼쪽에 있는 트럭을 제거하고, 그 트럭의 무게를 다리 위의 트럭들의 무게 합에서 빼줌
    if trucks:
        # 현재 다리 위에 있는 트럭들의 무게 합과 다음에 올 트럭의 무게 합이 다리의 최대 하중을 넘지 않으면,
        if total_weight + trucks[0] <= l:
            # 다음에 올 트럭을 다리 위에 올림
            total_weight += trucks[0]
            bridge.append(trucks.pop(0))
        # 다음에 올 트럭의 무게를 버틸 수 없으면,
        else:
            # 다리 위에 아무 것도 올리지 않음(0을 올림)
            bridge.append(0)

# 모든 트럭이 다리를 건너는 데에 걸린 시간 출력
print(time)
