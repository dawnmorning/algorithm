# 몇 번 테스트 할 것인지 입력 받기
T = int(input())
# T번만큼 돌리기 위해서는 for문이 필요
for i in range(T):
    #예제에서 입력을 띄워서 받기 때문에 정수형으로 분리해서 받기위해 split활용
    A, B = map(int, input().split())
    print(A + B)


