N = input()
for i in range(len(N)):
    if i % 10 == 9:
        print(N[i], end='\n')      #i는 계속 돌아가는 중,, 
    else:                          
        print(N[i], end='')

