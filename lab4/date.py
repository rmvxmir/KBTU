# Task 1
from datetime import datetime, timedelta
five_days_ago = datetime.now() - timedelta(days=5)
print(five_days_ago.strftime("%d-%m-%Y"))

# Task 2
yesterday = datetime.now() - timedelta(days=1)
today = datetime.now()
tomorrow = datetime.now() + timedelta(days=1)
print(yesterday.strftime("%d-%m-%Y"))
print(today.strftime("%d-%m-%Y"))
print(tomorrow.strftime("%d-%m-%Y"))

# Task 3
current_date = datetime.now()
result_date = current_date.replace(microsecond=0)
print(result_date.strftime("%d-%m-%Y %H:%M:%S"))

# Task 4
date1 = datetime.now()
date2 = datetime.now() - timedelta(days=3)
diff = date1 - date2
print(int(diff.total_seconds()))