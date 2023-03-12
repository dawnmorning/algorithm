# from math import comb

n, m = map(int, input().split())
# 1 ~ n까지 팩토리얼 값이 담길 공간
factorial_arr = [0 for _ in range(n+1)]
factorial_arr[1] = 1
for i in range(2, n+1):
    factorial_arr[i] = factorial_arr[i-1] * i

    # 조합 구하는 공식 nCm = n! // r! * (n-m)!
print(factorial_arr[n] // (factorial_arr[m] * factorial_arr[n-m]))