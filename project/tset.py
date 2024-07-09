# import time
# days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

# timestamp = time.time()
# current_date = time.ctime(timestamp)
# cd = current_date.split(' ')
# day = list(cd)

# hour = day[4].split(':')[0]
# idx = days.index(day[0])
# idx =  (idx) % len(days)
# print(f'idx {idx}')
# days[:] = days[idx:] + days[:idx]
# print(days)
# print(hour)
# print(day[0])
# # hour = [i for i in range(0, 24)]
# # hours = [[i for i in range(0, 24)]] * 7
# # hours[0] = [i for i in range(6, 24)]
# # print(hours)

# # dct = {'e': 1, 'r': 3}
# # if 'f' in dct.keys():
# #     print(dct['f'])

from datetime import datetime, timedelta

# Step 2: Example datetime object
original_datetime = datetime.now()

# Step 3: Number of days to add
days_to_add = 0

# Step 4: Create a timedelta object
delta = timedelta(days=days_to_add)

# Step 5: Add the timedelta to the original datetime
new_datetime = original_datetime + delta

# Step 6: The result
print("Original datetime:", original_datetime)
print("New datetime:", new_datetime)