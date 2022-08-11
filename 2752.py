n = list(map(int,input().split()))
for i in range(len(n)-1):
    for j in range(1,len(n)):
        if n[i] > n[j]:
            n[i], n[j] = n[j], n[i]
for i in n:
    print(i, end= ' ')