from itertools import combinations
n, m = map(int, input().split())
li = list(map(int, input().split()))
li = sorted(li)
for number in list(combinations(li,m)):
    for num in number:
        print(num, end= ' ')
    print()

