import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
blocks = list(input())
dp = [1e9 for _ in range(n)]
dp [0] = 0

for i in range(1,n):
    prev_shouting = "?"
    if blocks[i] =="O":
        prev_shouting = "B"
    if blocks[i] == "J":
        prev_shouting = "O"
    if blocks[i] == "B":
        prev_shouting = "J"
    for j in range(i):
        if blocks[j] == prev_shouting:
            dp[i] = min(dp[i], dp[j] + pow(i-j,2))
print(dp[n-1] if dp[n-1] != 1e9 else -1)
