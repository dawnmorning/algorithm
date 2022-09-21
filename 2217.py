import sys
sys.stdin = open('2217')
n = int(input())
li = []
maxli = []
for _ in range(n):
    can = int(input())
    li.append(can)
li = sorted(li, reverse=True)
for i in range(n):
    maxli.append(li[i] * (i +1))
print(max(maxli))
