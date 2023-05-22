n = int(input())
get_list = []
for i in range(n):
    get_list.append(input())
ret = sorted(set(get_list), key= lambda x : (len(x),x))
for j in ret:
    print(j)