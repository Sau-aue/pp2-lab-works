#1 strftime beatifull format
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))

#2 day:month:year
from datetime import datetime

now = datetime.now()
print(now.strftime("%d.%m.%Y"))

#3 дата + время часы:минуты
from datetime import datetime

now = datetime.now()
print(now.strftime("%d.%m.%Y %H:%M"))

#4 название дня недели
from datetime import datetime

now = datetime.now()
print(now.strftime("%A"))  # Monday, Tuesday...

#5 ISO формат (часто в проектах)
from datetime import datetime

now = datetime.now()
print(now.isoformat())