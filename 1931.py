import sys
sys.stdin = open('1931.txt')
input = sys.stdin.readline
n = int(input())
time = [list(map(int, input().split()))for _ in range(n)]
time = sorted(time, key=lambda x: x[0])
time = sorted(time, key =lambda x : x[1])
last, result = 0, 0
for i in time:
    if i[0] >= last:
        result += 1
        last = i[1]
print(result)

# print(time)
# maxC = 0
# for i in range(n):
#     cnt = 0
#     for j in range(i+1,n):
#         if time[i][1] < time[j][0]:
#             time[i] = time[j]
#             cnt += 1
#             if maxC < cnt:
#                 maxC = cnt
