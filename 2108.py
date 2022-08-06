import sys
from collections import Counter
n_list = []
n = int(sys.stdin.readline()) 
for i in range(n):
    num = int(sys.stdin.readline())
    n_list.append(num)
s = sorted(n_list)
num_s = Counter(s).most_common()
print(round(sum(n_list)/n))
print(s[n//2])
 #(대상숫자, 나온 횟수)
if len(num_s)>1: #두개 이상일 때
    if num_s[0][1] == num_s[1][1]: #서로가 같으면
        print(num_s[1][0]) # 두번째를 출력
    else: 
        print(num_s[0][0])
else:
    print(num_s[0][0])

print(sorted(n_list)[-1] - sorted(n_list)[0])

