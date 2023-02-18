import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    q = deque()
    q.append([a,''])
    visited = [False] * 10000
    visited[a] = True
    
    while q: 
        num, answer = q.popleft()
        if num == b : 
            print(answer)
            break

        d = (2 * num) % 10000
        if not visited[d]:
            q.append([d, answer+"D"])
            visited[d] = True
        
        s = (num - 1) % 10000
        if not visited[s]:
            q.append([s, answer+"S"])
            visited[s] = True
        
        l = num // 1000 + (num % 1000) * 10
        if not visited[l]:
            q.append([l, answer+"L"])
            visited[l] = True
        
        r = (num // 10 + (num%10) * 1000)% 10000
        if not visited[r]:
            q.append([r, answer+"R"])
            visited[r] = True