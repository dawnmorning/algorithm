from itertools import combinations_with_replacement
n, m = map(int, input().split())
li = list(range(1,n+1))
xx = list(combinations_with_replacement(li,m))
for x in xx:
    print(*x)