import sys
input = sys.stdin.readline
example = input().upper().rstrip()
li = list(set(example))
answer = []

for i in li:
    cnt = example.count(i)
    answer.append(cnt)

if answer.count(max(answer)) >= 2:
    print("?")
else:
    print(li[(answer.index(max(answer)))].upper())
