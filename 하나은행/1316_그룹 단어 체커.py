n = int(input())

for _ in range(n):
    test = input()
    for i in range(len(test)-1):
        if test[i] != test[i+1]:
            if test[i+1] in test[:i+1]:
                n -= 1
                break
print(n)


