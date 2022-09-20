import sys
sys.stdin = open('16987.txt')
input = sys.stdin.readline
n = int(input())
eggs = [list(map(int, input().split()))for _ in range(n)]
def dfs(idx):
    if idx == n:
        cnt = 0
        for d, w in eggs:
            if d <= 0:
                cnt += 1
        return cnt

    if eggs[idx][0] <= 0:
        return dfs(idx+1)
    for i in range(n):
        if i == idx:
            continue
        if eggs[i][0] > 0:
            break
    else:
        return dfs(idx+1)

    maxV = 0
    for i in range(n):
        if i == idx:   # 째는게 시간 덜 걸림
            continue
        if eggs[i][0] <= 0:
            continue
        eggs[i][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]

        maxV = max(maxV, dfs(idx+1))

        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]
    return maxV

print(dfs(0))


