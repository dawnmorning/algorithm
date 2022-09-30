# kruskal
import sys

sys.stdin = open('1197.txt')


def findset(rep_list,x):
    while rep_list[x] != x:
        x = rep_list[x]
    return x

def union(rep_list, a ,b):
    a = findset(rep_list,a)
    b = findset(rep_list,b)
    if a<b:
        rep_list[b] = a
    else:
        rep_list[a] = b

V,E = map(int, input().split())
rep_list = [i for i in range(V+1)]
edges = []
result = 0
for _ in range(E):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key = lambda x : x[2])
for edge in edges :
    a,b,cost = edge
    if findset(rep_list, a) != findset(rep_list,b):
        union(rep_list,a,b)
        result += cost
print(result)