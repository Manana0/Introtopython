import datetime
import calendar
import time
current = datetime.datetime.now()
print ("Current time:", current)
print('Year: ', current.year)
print('Month: ', current.month)
print('Day: ', current.isoweekday())
delta = datetime.timedelta(days = 5)
print( current - delta)
print( current + delta)
