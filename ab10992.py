n = int(input())
for i in range(1,n+1):
    if i == 1:
        print(' '*(n-1)+'*')
    elif i == n:
        print(((2 * i) - 1)*'*')
    else:
        print(' ' * (n-i) + ('*') + (' ' * ((i-1) * 2 - 1)) + ('*'))
