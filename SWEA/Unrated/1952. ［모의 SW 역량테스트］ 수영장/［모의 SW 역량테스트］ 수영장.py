def min_money(idx,money):
    global minV
    if idx >= 12:
        if minV > money:
            minV = money
        return minV

    for i in range(4):
        if i == 0:
            min_money(idx+1, money+ fare[i] * plan[idx])
        if i == 1:
            min_money(idx+1, money + fare[i])
        if i == 2:
            min_money(idx+3, money + fare[i])
        if i == 3:
            min_money(idx+1, fare[i])

t = int(input())
for tc in range(1, t+1):
    fare = list(map(int, input().split())) # [10, 40, 100, 300]
    plan = list(map(int, input().split())) # [0, 0, 2, 9, 1, 5, 0, 0, 0, 0, 0, 0]
    minV = 3000 ** 12
    min_money(0,0)
    print(f'#{tc} {minV}')