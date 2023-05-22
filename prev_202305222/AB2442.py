N = int(input())
for i in range(N+1):
    ans = " " * (N-i) + '*' * ((2*i)-1)
    print(ans)