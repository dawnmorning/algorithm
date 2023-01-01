import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
answer = [0]

temp = 0
for i in arr:
    temp += i
    answer.append(temp)
for i in range(m):
    s,e = map(int, input().split())
    print(answer[e] - answer[s-1])

# for _ in range(m):
#     s,e = map(int, input().split())
#     value = 0
#     temp = []
#     for i in range(s-1,e):
#         value += arr[i]
#     temp.append(value)
# print(answer)
