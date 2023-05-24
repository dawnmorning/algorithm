n = int(input())
stack = []
answer = []
isFind = True
count = 1
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        isFind = False
if not isFind:
    print('NO')
else:
    for i in answer:
        print(i)