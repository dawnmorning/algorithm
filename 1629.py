a,b,c = map(int,input().split())
def cal(a, b,c):
    if b == 1:
        return a % c
    value = cal(a, b//2,c)
    if b % 2 == 1:
        return ((value**2)*a) % c 
    else:
        return (value**2) % c   
print(cal(a,b,c))
# a,b,c = map(int,input().split())
# n=( a ** b ) % c
# print(n)