# 몇 번 테스트 할 것인지 입력 받기
T = int(input())
count = 0
# T번만큼 돌리기 위해서는 for문이 필요
for i in range(T):
    #예제에서 입력을 띄워서 받기 때문에 정수형으로 분리해서 받기위해 split활용
    count+=1
    A, B = map(int, input().split())
    C = A + B
    #f-string을 쓸거기 때문에 중괄호에 들어갈 변수 지정
    print(f'Case #{count}: {C}')