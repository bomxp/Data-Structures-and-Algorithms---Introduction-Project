"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Part A
receiver_phone_list = list()
for call in calls:
    # The calls were initiated by "(080)"
    if call[0].startswith("(080)"):
        receiver_phone_list.append(call[1])

code_list = list()
for phone_num in receiver_phone_list:
    # Fixed lines
    if phone_num.startswith("(0"):
        code = re.findall(r'\((.*?)\)', phone_num)
        code_list.extend(code)
    # Mobile number
    if '(' not in phone_num and ')' not in phone_num and phone_num[5] == ' ' and (
            phone_num.startswith('7') or phone_num.startswith('8') or phone_num.startswith('9')):
        code_list.append(phone_num[0:4])
    # Telemarketer's number
    if '(' not in phone_num and ')' not in phone_num and ' ' not in phone_num and phone_num.startswith("140"):
        code_list.append("140")

print("The numbers called by people in Bangalore have codes:")
for sorted_code in sorted(set(code_list)):
    print(sorted_code)

# Part B
same_state_counter = 0
for phone in receiver_phone_list:
    if phone.startswith("(080)"):
        same_state_counter += 1
bangalore_percentage = float(same_state_counter) / len(receiver_phone_list)
print("{:.2%}".format(bangalore_percentage),
      "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
