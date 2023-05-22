import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    vps = list(input())
    total = 0

    for i in vps: 
        if i == "(":
            total +=1
        elif i == ")":
            total -=1
        if total<0:
            print("NO")
            break

    if total == 0:
        print("YES")
    elif total>0:
        print("NO")