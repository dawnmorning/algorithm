n = int(input())
m=n
for i in range(1,n+1):
    print(' ' * (n-i)+ '*'*(i))
for j in range(1,m):
    print(' '* j + '*' * (m-j))