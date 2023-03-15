n,m = map(int, input().split())
answer = []
def backtracking():
    if len(answer) == m:
        print(*answer)
        return
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            backtracking()
            answer.pop()
backtracking()