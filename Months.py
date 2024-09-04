import datetime as dt
import calendar

current_time = dt.datetime.now()
today = dt.date.today()

year = 2011
month = 9

print(f"The current time GST : {current_time} ")
print(f"Today GST : {today}")

print(calendar.month(year, month))
print(calendar.month(2011, 9))

