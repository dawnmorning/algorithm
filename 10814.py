import sys
input = sys.stdin.readline

# n = int(input())
# online_name = []
# online_old = []
# for i in range(n):
#     a,b = input().split()
#     a = int(a)
#     online_old.append(a)
#     online_name.append(b)
# s_old = sorted(online_old)
# for j in range(n):
#     print(s_old[j], online_name[j])

count = int(input())
mem_list = []
for _ in range(count):
    age, name = input().split()
    age = int(age)
    mem_list.append([age, name])
mem_list.sort(key=lambda x: x[0])

for i in list:
    print(i[0], i[1], sep=' ')


