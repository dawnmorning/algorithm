li = []
lii = []
for _ in range(8):
    a = int(input())
    li.append(a)
    lii.append(a)

li = sorted(li, reverse=True)
print(sum(li[:5]))
temp = []
for j in range(5):
    for i in range(len(li)):
        if li[j] == lii[i]:
            temp.append(i+1)
for k in sorted(temp):
    print(k, end = ' ')
