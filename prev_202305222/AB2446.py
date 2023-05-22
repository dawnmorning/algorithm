# n = int(input())
# for i in range(2*n-1):
#     if i < n :
#         print(' ' * (i) + '*' * (2*(n-i) -1) + ' '* (i))
#     else : 
#         print(' ' * ((2*n)-i-2) + '*' * (2*i - 2*n +3) + ' ' * (2 * n)-i-2)

a = int(input())
b=a
for i in range(1,a+1):
    print(' '*(i-1) + '*'*(2*(b-i)+1))
for k in range(1,b):
    print(' ' * (b-k-1) + '*' * (2*k+1))