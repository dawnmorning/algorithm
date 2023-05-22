x, y = map(int,input().split())
month = ["SUN","MON",'TUE','WED','THU','FRI','SAT']
day = [31,28,31,30,31,30,31,31,30,31,30,31]
date = 0
for i in range(x-1):
    date += day[i]
    print(date)
date = (date + y) % 7
print(month[date])