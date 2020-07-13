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

numbers_doing_marketing = set()
# regular_numbers = set()
# for call in calls:
#     numbers_doing_marketing.add(call[0])
#     regular_numbers.add(call[1])
# for text in texts:
#     regular_numbers.add(text[0])
#     regular_numbers.add(text[1])
# numbers_doing_marketing.difference_update(regular_numbers)
for call in calls:
    numbers_doing_marketing.add(call[0])
for call in calls:
    numbers_doing_marketing.discard(call[1])
for text in texts:
    numbers_doing_marketing.discard(text[0])
    numbers_doing_marketing.discard(text[1])
print("These numbers could be telemarketers: ")
for number_to_print in (sorted(numbers_doing_marketing)):
    print(number_to_print)
