import datetime

x,y = map(int,input().split())
date = datetime.date(2007,x,y)

day_of_week = date.strftime("%A")
ans = day_of_week.upper()

print(ans[:3])
