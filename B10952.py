while True:
    A, B = map(int, input().split())
    if A==0 and B==0 :
        break
    else:
        print(A+B)

# 기본적으로 지속적인 테스트를 받다가, A가 0을 받고, B가0을받는다면 입력만 뜨게하고 출력이 나오지 않게 break!!
    