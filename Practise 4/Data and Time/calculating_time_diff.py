#1 разница между двумя датами
from datetime import date

d1 = date(2026, 2, 27)
d2 = date(2026, 3, 5)
print(d2 - d1)  # how many days

#2 сколько дней как число
from datetime import date

d1 = date(2026, 2, 27)
d2 = date(2026, 3, 5)
diff = d2 - d1
print(diff.days)

#3 прибавить 7 дней
from datetime import date, timedelta

today = date.today()
print(today + timedelta(days=7))

#4 прибавить 2 часа 30 минут
from datetime import datetime, timedelta

now = datetime.now()
later = now + timedelta(hours=2, minutes=30)
print(later)

#5 засечь время выполнения
from datetime import datetime

start = datetime.now()

total = 0
for i in range(1_000_000):
    total += i

end = datetime.now()
print("Time:", end - start)
