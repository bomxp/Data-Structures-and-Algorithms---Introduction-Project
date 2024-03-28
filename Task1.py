"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Python set is not allow duplicate, use it
result_set = set()
# Add all phone number to set
for text in texts:
    result_set.add(text[0])
    result_set.add(text[1])
for call in calls:
    result_set.add(call[0])
    result_set.add(call[1])
# Get result
print("There are",len(result_set),"different telephone numbers in the records.")