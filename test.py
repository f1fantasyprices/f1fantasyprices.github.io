from datetime import datetime

now = datetime.now()
time = datetime(now.year, now.month, now.day, now.hour)
print(time)