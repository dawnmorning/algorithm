import sys
from collections import deque
input = sys.stdin.readline
tc = int(input())
for t in range(tc):
    flag = 0
    func = list(input())
    n = int(input())
    # 미친 rstrip
    dq = deque(input().rstrip()[1:-1].split(","))
    if n == 0:
        dq = deque()
    for i in range(len(func)):
        if func[i] == 'R':
            flag += 1
        elif func[i] == 'D':
            if len(dq) >= 1:
                if flag%2==0:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                print('error')
                break
    else:
        if flag % 2 == 1:
            dq.reverse()
            print("["+ ",".join(dq) + "]")
        else:
            print("[" + ",".join(dq) + "]")
