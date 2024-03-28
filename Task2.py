"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# List call with time spend
phone_with_time_spend_list = list(list())
for call in calls:
    phone_with_time_spend_list.append([call[0], call[3]])
    phone_with_time_spend_list.append([call[1], call[3]])

# Create dict for remove duplicate phone num and adding time spend
phone_with_time_dict = {}
for phone_with_time in phone_with_time_spend_list:
    phone_num = phone_with_time[0]
    time_spend = int(phone_with_time[1])
    # Phone num present in dict
    if phone_num in phone_with_time_dict:
        # Update dict adding time spend
        phone_with_time_dict.update({phone_num: phone_with_time_dict.get(phone_num) + time_spend})
    # Phone num not present in dict, add them
    else:
        phone_with_time_dict[phone_num] = time_spend
# Find max result by time spend
(max_phone, max_time_spend) = max(phone_with_time_dict.items(), key=lambda x: x[1])

print(max_phone, "spent the longest time,", max_time_spend, "seconds, on the phone during September 2016.")
