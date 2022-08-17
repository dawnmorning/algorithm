import sys
sys.stdin = open('9934.txt')
# input = sys.stdin.readline
k = int(input())
li = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def wood(arr,x):
    mid = (len(arr)//2)
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    wood(arr[:mid], x+1)
    wood(arr[mid+1:],x+1)

wood(li, 0)
for i in range(k):
    print(*tree[i])
