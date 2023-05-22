A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = b = 0
for i in range(len(A)):
    a += A[i]
    if a>b :
        print('Yes')
        break
    b += B[i]
else:
    print('No')