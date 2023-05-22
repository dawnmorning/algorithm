import sys
input = sys.stdin.readline
example = list(map(int, input().split()))
ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]
if example == ascending:
    print('ascending')
elif example == descending:
    print('descending')
if example != ascending and example != descending:
    print('mixed') 
