n = input()
vowel = []
for i in n:
    vowel.append(int(i))
value = sorted(vowel, reverse = True)
for i in value:
    print(i,end='')
