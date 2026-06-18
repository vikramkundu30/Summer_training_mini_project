import datetime
year=2000
month=6
day=16
a=datetime.date(year,month,day)
b=datetime.date.today()
c=b.year-a.year
d=b.month-a.month
e=b.day-a.day
if e<0:
  d=d-1
  e=30+e
if d<0:
  c=c-1
  d=12+d
print(c,d,e)
print("Total month",(c*12)+d)
print("Total day",(c*365)+(d*30)+e)
