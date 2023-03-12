n,m = map(int, input().split())
# 순서가 상관이 없는 문제
answer = []

def dfs(start):
    if len(answer) == m : 
        print(''.join(map(str, answer)))
        return
    for i in range(start, n+1):
        if i not in answer:
            answer.append(i)
            dfs(i + 1)
            answer.pop()

dfs(1)