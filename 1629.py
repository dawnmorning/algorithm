a,b,c = map(int,input().split())
# def cal(a, b,c):
#     if b == 1:
#         return a % c
#     value = cal(a, b//2,c)
#     if b % 2 == 1:
#         return ((value**2)*a) % c 
#     else:
#         return (value**2) % c   
# print(cal(a,b,c))
def cal(a, b, c):
    value = 1
    while b:
        if b == 1:
            return a % c
        if b % 2 == 1: value *= a
        a = a * a
        b //= 2
    return value % c

print(cal(10, 11, 12))