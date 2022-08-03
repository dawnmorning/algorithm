n = int(input())

value = 0
for j in range(n):
    a,b = map(int,input().split())
    for i in range(1,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            value = i
    print(a*b//value)