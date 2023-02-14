n,m = map(int, input().split())
not_hear = set()
not_see = set()

for i in range(n):
    hear_list = input()
    not_hear.add(hear_list)
for j in range(m):
    see_list = input()
    not_see.add(see_list)
hear_see= sorted(list(not_hear&not_see))
# print(len(hear_see), *hear_see,sep="\n")
print(len(hear_see))
for s in hear_see:
    print(s)
