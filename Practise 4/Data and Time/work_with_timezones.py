#1 UTC time
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc)

#2 сделать “aware” datetime (с timezone)
from datetime import datetime, timezone

dt = datetime(2026, 2, 27, 12, 0, tzinfo=timezone.utc)
print(dt)

#3 Алматы timezone через zoneinfo
from datetime import datetime
from zoneinfo import ZoneInfo

now_almaty = datetime.now(ZoneInfo("Asia/Almaty"))
print(now_almaty)

#4 конвертация Алматы → UTC
from datetime import datetime
from zoneinfo import ZoneInfo

almaty = datetime.now(ZoneInfo("Asia/Almaty"))
utc = almaty.astimezone(ZoneInfo("UTC"))
print("Almaty:", almaty)
print("UTC:", utc)

#5 два города сравнить (Алматы и Токио)
from datetime import datetime
from zoneinfo import ZoneInfo

almaty = datetime.now(ZoneInfo("Asia/Almaty"))
tokyo = datetime.now(ZoneInfo("Asia/Tokyo"))

print("Almaty:", almaty.strftime("%H:%M"))
print("Tokyo:", tokyo.strftime("%H:%M"))



