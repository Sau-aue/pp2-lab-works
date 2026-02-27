#1 time now
from datetime import datetime

now = datetime.now()
print(now)

#2 only data
from datetime import date

today = date.today()
print(today)

#3 only time(hour:min:sec)
from datetime import datetime

t = datetime.now().time()
print(t)

#4 time (year:month:day)
from datetime import datetime

now = datetime.now()
print(now.year, now.month, now.day)

#5 change part of the time
from datetime import datetime

now = datetime.now()
changed = now.replace(year=2030, month=12)
print(changed)