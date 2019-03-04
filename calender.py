import calendar
y=int(input())

x=calendar.weekday(y,1,1)
d=calendar.day_name[x]
d=d.lower()
print(d)