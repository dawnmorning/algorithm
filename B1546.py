N = int(input())
scores = list(map(int, input().split())) #N개 만큼만 입력을 받음
M = max(scores)
all_scores = 0
for i in scores:
    all_scores += (i / M) * 100
new_average = all_scores / len(scores)
print(new_average)