# n = int(input())
# def f(n):
#     value = 0
#     if n == 0: 
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         value += f(n-1) + f(n-2)
#     return value
# print(f(n)) 시간초과

n = int(input())
fiboniacci = []
num = 0
for i in range(n+1):
    if i == 0:
        num = 0
    elif i <= 2:
        num = 1
    else : 
        num = fiboniacci[-1] + fiboniacci[-2]
    fiboniacci.append(num)
print(fiboniacci[-1])     
