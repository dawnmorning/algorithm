#계속 돌리기 위해서는 while True : 가 필요 
#입력은 여러 개의 테스트 케이스로 이루어져있다!!!
#무한루프가 돌아가버리니까 -> 런타임 에러가 뜬다.. 이를 해결하기 위해
#try except구문을 통해 어떤 예외값이 입력되면 강제로 종료하게 만들기
while True:
    try :
        A, B = map(int, input().split())
    except:
        break
    print(A + B)