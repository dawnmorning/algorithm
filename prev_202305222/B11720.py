# 몇개까지 까지 계산할거니? -> for문으로 
N = int(input())
# 
A = map(int, input())
total = 0
for j in A:  # 근데 여기서는 어차피 숫자 갯수가 j만큼 돌아가므로 따로 실행 횟수 정하지 않아도 됨
    total += j
print(total)

        