import sys
input = sys.stdin.readline

x,y,w,h = map(int, input().split())
vacant_list = []
vacant_list.append(x)
vacant_list.append(y)
vacant_list.append(abs(x-w))
vacant_list.append(abs(y-h))
print(min(vacant_list))

# if abs(x-w) < abs(y-h):
#     if abs(x-w) < x :
#         print(abs(x-w))
#     else:
#         print(x)
# elif abs(y-h) < abs(x-w):
#     if abs(y-h) < y:
#         print(abs(y-h))
#     else:
#         print(y)