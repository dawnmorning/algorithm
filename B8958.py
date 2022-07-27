N = int(input())
for i in range(N) : # 받은 N만큼 test case를 돌려야 하므로 필요하다!
    n_list = list(input()) #리스트 형태로 받아 하나씩 조건과 일치할 때 어떻게 할지 정함 
    sum = 0 
    c = 1
    for i in n_list:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)