from collections import deque

def solve(a,b):
    # 값, 시작 cnt
    q = deque([(a,1)])
    while q:
        a, cnt = q.popleft()
        if a == b:
            print(cnt)
            break
        # 2를 곱해서 나올 수 있는 값들 추가
        if a*2 <= b:
            q.append((a*2, cnt+1))
        # 오른족에 1을 붙이는 방법은 나온값에 * 10 + 1 
        if a * 10 + 1 <= b:
            q.append((a*10+1, cnt + 1))
        if not q:
            print(-1)

a,b = map(int, input().split())
solve(a,b)
