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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = set([x[0] for x in calls])
call_receiver = [x[1] for x in calls]
text_sender = [x[0] for x in texts]
text_receiver = [x[1] for x in texts]

possible_telemarketers_set = set()
for caller in callers:
    if caller not in set(call_receiver + text_sender + text_receiver):
        possible_telemarketers_set.add(caller)

print("These numbers could be telemarketers: ")
for phone in sorted(possible_telemarketers_set):
    print(phone)
