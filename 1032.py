n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
# print(arr[0]) : config.sys
# print(arr[0][0]) : c
result = list(arr[0])
for i in range(n):
    for j in range(len(arr[0])):
        if result[j] == arr[i][j]:
            continue
        else:
            result[j] = "?"
print(''.join(result))