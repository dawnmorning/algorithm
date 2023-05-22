import sys
n,m = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
s = sorted(li)
print(s[m-1])

#오른쪽으로 입력 받을 때는 for문 필요없이
