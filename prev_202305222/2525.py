a,b = map(int, input().split())
c = int(input())
# if c >= 60:
#     a = c//60 + a
#     b = c % 60 + b
# else:
#     b = b + c
# print(a,b)

total = a*60 + b+ c
hour = 0
minute = 0

if total // 60 >= 24:
    hour = total // 60 -24
    minute = int(total%60)
else:
    hour = total//60
    minute = int(total%60)
print(hour,minute)

