import datetime
import calendar
import time
bday = datetime.date(2020, 5, 17)
print(bday)
print(bday.year)
print(bday.month)
print(bday.day)
print(bday.isoweekday())
today = datetime.date.today()
days = bday - today
print(days)
cal = calendar.month(2017, 5)
print(cal)
now=datetime.datetime.now()
delta = datetime.timedelta(days = 1)
y=now - delta
print(y)
delta2 = datetime.timedelta(days = 2)
print(y+ delta2)
delta3 = datetime.timedelta(days = 3)
print(y- delta3)