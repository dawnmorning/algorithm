s = int(input())

count = 0
answer = 0
for i in range(1,s+1):
    answer += i
    count += 1
    if(answer > s):
        count -= 1
        break
print(count)
    