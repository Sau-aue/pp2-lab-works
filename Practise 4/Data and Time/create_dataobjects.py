#1 make date
from datetime import date

d = date(2026, 2, 27)
print(d)

#2 make datatime(date+time)
from datetime import datetime

dt = datetime(2026, 2, 27, 14, 30, 0)
print(dt)

#3 make date отдельно
from datetime import time

t = time(9, 15, 0)
print(t)

#4 to make date from str by strptime
from datetime import datetime

dt = datetime.strptime("2026-02-27", "%Y-%m-%d")
print(dt)

#5 создать дату “сегодня” + руками добавим время
from datetime import date, datetime

today = date.today()
dt = datetime.combine(today, datetime.now().time())
print(dt)
