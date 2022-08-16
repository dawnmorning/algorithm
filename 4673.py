natural = set(range(1,10001))
non_natural = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    non_natural.add(i)
self_num = sorted(natural - non_natural)
for i in self_num:
    print(i)