test = input()
# count = 0
arr=["c=","c-","dz=","lj","nj","s=","z=","d-"]
for i in arr:
    if i in test:
        test.replace(i,"*")
print(len(test))
