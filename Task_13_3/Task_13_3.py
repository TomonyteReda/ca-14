import datetime as dt
# from datetime import date
from datetime import date as data

today = dt.datetime.now()
print(today)
today_date = dt.datetime.today().date()
print(today_date)
today_time = today.strftime("%H:%M:%S")
print(today_time)
# today_2 = date.today()
# print(today_2)
today_3 = data.today()
print(today_3)


